from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def student_profile():
    return render_template(
        "profile.html",
        name="souvik",
        is_student=True,
        courses=["Python", "Java", "C++"],)
