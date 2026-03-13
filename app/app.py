from flask import Flask, render_template, request
from functions/rbac import create_user

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/create-user", methods=["POST"])
def user():
    username = request.form["username"]
    namespace = request.form["namespace"]

    create_user(username, namespace)

    return "User created"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
