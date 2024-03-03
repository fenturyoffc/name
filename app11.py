from flask import Flask, render_template, request, redirect


app = Flask(__name__)

username = ""

@app.route("/")
def index():
    return render_template("index.html", name=username)

@app.route("/hello", methods=["POST"])
def hello():
    global username
    username = request.form.get("name")
    return redirect("/")



if __name__ == "__main__":
    app.run(port=8080)