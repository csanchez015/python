from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template("level1.html")

@app.route('/play/<x>')
def play2(x):
    number = int(x)
    return render_template("level2.html", number = number)

@app.route('/play/<x>/<color>')
def play3(x, color):
    number = int(x)
    changeColor = color
    return render_template("level3.html", number = number, changeColor = changeColor)

if __name__== "__main__":
    app.run(debug=True)



