from flask import Flask, render_template, request, redirect, url_for,flash
from My_site_2 import RegistrationForm
app = Flask(__name__, template_folder='My_site')
app.secret_key = 'my_secret_key'

@app.route('/', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if request.method == "POST":
        if form.validate_on_submit():
            name = form.name.data
            email = form.email.data
            flash(f" Welcome {name}! Your form has been registered  successfully.")
            return redirect(url_for('success'))
        
    return render_template('register.html', form=form)

@app.route('/success')
def success():
    return render_template('success.html')