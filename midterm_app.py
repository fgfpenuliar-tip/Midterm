from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def login():
    return render_template("login.html")

@app.route("/register/", methods=["GET"])
def register():
    return render_template("register.html")

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)