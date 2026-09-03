from flask import Flask, render_template, request, redirect, url_for,flash
app = Flask(__name__, template_folder='template_3')
app.secret_key = 'forms_secret_key'

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == "POST":
        name=request.form.get("name")
        if not name:
            flash("Name is required!", "error")
            return redirect(url_for('form'))
        flash(f"Form submitted successfully!{name}")
        return redirect(url_for('thankyou'))
    return render_template('form.html')


@app.route("/thankyou")
def thankyou():
    return render_template('thankyou.html')
