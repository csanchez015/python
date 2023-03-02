from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "WOWTHESECRETKEY"

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 0
    else:    
        session["count"] += 1
    return render_template("counter.html")

@app.route("/count", methods=["POST"])
def count():
    if request.form["clicker"]=="add":
        session["count"] += 1
    elif request.form["clicker"]=="reset":
        session["count"] = 0
    return redirect("/")

@app.route("/destroy_session")
def destroy_session():
    session.clear()
    return redirect("/")
    
if __name__=="__main__":
    app.run(debug=True) 