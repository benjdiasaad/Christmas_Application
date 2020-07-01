from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline="BENJDIA Saad"
    return render_template("index.html", headline=headline)

#j'ai changé la valeur que je transmets comme titre

@app.route("/bye")
def bye():
    headline="ziad idrissi"
    return render_template("index.html", headline=headline)