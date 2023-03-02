from flask import Flask, render_template, request,redirect, session
app = Flask(__name__)
app.secret_key = "matrix"
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dashboard')
def index15():
    return "<h1>heres the redirect mofo</h1>"

@app.route('/users', methods=['post'])
def index1():
    print(request.form)
    return redirect('/dashboard')

@app.route('/add_to_session')
def add_session():
    session["name"] = "Hardcoded game"
    return redirect("/dashboard")


if __name__ == "__main__":
    app.run(debug=True)