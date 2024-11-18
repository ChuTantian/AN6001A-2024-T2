from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return(render_template("index.html"))

@app.route("/", methods=["GET", "POST"])
def index():
    name = request.form.get("q")
    return(render_template("main.html"))

if __name__ == "__main__":
    app.run()
