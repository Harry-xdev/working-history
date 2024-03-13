from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/button-click", methods=["POST"])
def button_click():
    return "Chấm tăng ca rồi nha."

if __name__ == "__main__":
    app.run(port=5500)