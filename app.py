from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock database of user credentials (for demonstration purposes)
users = {
    'user@example.com': {'password': 'password123'}  # Mock user email and password
}

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

    # Check if email and password are correct
    if email in users and users[email]['password'] == password:
        return redirect(url_for('index'))  # Redirect to the index page if login is successful
    else:
        return "Invalid email or password. Please try again."

# Signup page route
@app.route("/signup")
def signup():
    return render_template("signup.html")

# Handle signup form submission
@app.route("/signup", methods=["POST"])
def handle_signup():
    # Get the form data (name, email, password, and re-entered password)
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    confirmPassword = request.form.get("confirmPassword")

    # Check if passwords match
    if password != confirmPassword:
        return "Passwords do not match. Please try again."

    # Save user credentials (in a real app, you would save them in a database)
    users[email] = {'password': password}  # Store the new user's credentials
    return redirect(url_for('login'))  # Redirect to the login page after signup

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
