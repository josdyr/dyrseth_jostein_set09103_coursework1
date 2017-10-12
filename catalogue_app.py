from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("template.html")


app.run(debug=True, port=8000, host='0.0.0.0')
