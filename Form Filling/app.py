from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit_form():
    # Collect form data
    data = {field: request.form.get(field) for field in request.form}

    # Pass the data to the success page
    return render_template("success.html", **data)

if __name__ == "__main__":
    app.run(debug=True)
