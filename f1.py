from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/about")
def jeetu():
    name = "jeetu"
    return render_template("about.html", Name = name)

app.run(debug=True)
