document.addEventListener("DOMContentLoaded", () => {
    // Check if SpeechRecognition and SpeechSynthesis are available
    if (!('SpeechRecognition' in window || 'webkitSpeechRecognition' in window)) {
        alert("Speech Recognition is not supported by your browser.");
        return;
    }

    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = 'en-IN';
    recognition.interimResults = false;

    const synth = window.speechSynthesis;

    const speakText = (text, callback) => {
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = "en-IN";
        utterance.onend = callback; // Trigger the callback when speech ends
        synth.speak(utterance);
    };

    // Welcome message
    speakText("Welcome to the Infosys University. Please fill out the following details for your course.", () => {});

    const micButtons = document.querySelectorAll(".mic-btn");

    micButtons.forEach((button) => {
        button.addEventListener("click", () => {
            const fieldId = button.dataset.field;
            const field = document.getElementById(fieldId);

            // First speak the prompt to the user
            speakText(`Please say your ${fieldId}`, () => {
                // After speech synthesis ends, start the recognition
                recognition.start();
            });

            recognition.onresult = (event) => {
                let speechResult = event.results[0][0].transcript.trim();

                // Remove trailing dot (.) for all fields
                speechResult = speechResult.replace(/\.$/, "");

                // Add % symbol for the percentage field
                if (fieldId === "percentage") {
                    speechResult = speechResult.replace(/[^0-9]/g, ""); // Ensure only numbers
                    speechResult += "%"; // Add % at the end
                }

                field.value = speechResult; // Update the form field

                // Speak confirmation after user has spoken and input is filled
                speakText(`You entered ${speechResult} for ${fieldId}`);
            };

            recognition.onerror = (event) => {
                console.error("Speech recognition error:", event.error);
                speakText("Error with speech recognition. Please try again.");
            };

            recognition.onend = () => {
                console.log("Speech recognition ended.");
            };
        });
    });
});
