from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/contatos")
def user():
    return render_template("contato.html")

@app.route("/sobre")
def who():
    return render_template("sobre.html")

if __name__ == "__main__":
    app.run (debug = True)