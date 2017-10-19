from flask import Flask, render_template
import json
# import data_Hardware
# import pprint
# import http.client


app = Flask(__name__)


with open('static/data/popular_movies.json') as in_file:
    movie_dict = json.load(in_file)
    in_file.close()
    # import pdb
    # pdb.set_trace()

img_path = 'http://image.tmdb.org/t/p/'
img_size = ["w92", "w154", "w185", "w342", "w500", "w780", "original"]
backdrop_size = ["w300", "w780", "w1280", "original"]


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html",
                           movies=movie_dict['results'],
                           img_path=img_path,
                           img_size=img_size,
                           backdrop_size=backdrop_size
                           )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
