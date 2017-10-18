from flask import Flask, render_template
import json
# import data_Hardware
# import pprint
# import http.client


app = Flask(__name__)


with open('static/data/data_4_movies.json') as in_file:
    movie_dict = json.load(in_file)
    in_file.close()
    # import pdb
    # pdb.set_trace()

img_path = 'http://image.tmdb.org/t/p/w342'


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html",
                           movies=movie_dict['results'],
                           img_path=img_path
                           )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
