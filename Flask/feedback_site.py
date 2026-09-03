from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates_2')

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/feedback', methods=['POST', 'GET'])
def feedback():
    if request.method == "POST":
        username = request.form.get('username')
        feedback = request.form.get('feedback')
        # Process the feedback (e.g., save to database, etc.)
        return render_template('thankyou.html', username=username, feedback=feedback)
    return render_template('feedback.html') 