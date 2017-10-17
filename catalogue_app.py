from flask import Flask, render_template
import json
import pprint

app = Flask(__name__)


with open('templates/index.html') as data_file:
    data = json.load(data_file)
pprint(data)


@app.route("/")
@app.route("/index")
def index():
    names = ['simon', 'thomas', 'lee', 'jamie', 'sylvester']
    return render_template("templates/index.html", title="Home|", names=names)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
