from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route (Login page)
@app.route("/")
def login():
    return render_template("login.html")

# Handle login form submission
@app.route("/login", methods=["POST"])
def handle_login():
    # Get the form data (name, email, and password)
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    # Check if all fields are filled
    if name and email and password:
        return redirect(url_for('index'))  # Redirect to the index page if all fields are filled
    else:
        return "Please fill in all fields"  # Return an error if any field is missing

# Index page
@app.route("/index")
def index():
    return render_template("index.html")

# Handle form submission for Infosys University Application
@app.route("/submit", methods=["POST"])
def submit_form():
    # Get the form data
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    dateofbirth = request.form.get("dateofbirth")
    city = request.form.get("city")
    pincode = request.form.get("pincode")
    state = request.form.get("state")
    nationality = request.form.get("nationality")
    religion = request.form.get("religion")
    gender = request.form.get("gender")
    university = request.form.get("university")
    course = request.form.get("course")
    percentage = request.form.get("percentage")
    preferredcourse = request.form.get("preferredcourse")

    # Render the success page with the submitted details
    return render_template(
        "success.html", 
        name=name, email=email, phone=phone, dateofbirth=dateofbirth, 
        city=city, pincode=pincode, state=state, nationality=nationality,
        religion=religion, gender=gender, university=university, 
        course=course, percentage=percentage, preferredcourse=preferredcourse
    )

if __name__ == "__main__":
    app.run(debug=True)
