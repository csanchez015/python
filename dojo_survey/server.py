from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "hellothere"

@app.route('/')
def index():
    return render_template("survey.html")

@app.route('/user_data')
def user_data():
    return render_template("result.html")

@app.route('/results', methods =['POST'])
def user_result():
    session["name"] = request.form['your_name']
    session["location"] = request.form['location']
    session["language"] = request.form['language']
    session["comment"] = request.form['comment']
    return redirect('/user_data')

if __name__=="__main__":
    app.run(debug=True)