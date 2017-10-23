from flask import Flask, render_template, request, redirect, url_for
import json


app = Flask(__name__)


user_logged_in = False


with open('static/data/popular_movies.json') as in_file:
    movie_dict = json.load(in_file)
    in_file.close()

img_path = 'http://image.tmdb.org/t/p/'
img_size = ["w92", "w154", "w185", "w342", "w500", "w780", "original"]
backdrop_size = ["w300", "w780", "w1280", "original"]


@app.route("/")
@app.route("/popular", methods=['GET', 'POST'])
def popular():
    if request.method == 'POST':
        data = request.form
        with open('static/data/users_info.json', 'w') as outfile:
            json.dump(data, outfile)
        return render_template('thank_you.html')
    elif request.method == 'GET':
        email = request.args.get('email')
        password = request.args.get('password')

        # read from .json file
        with open('static/data/users_info.json') as infile:
            new_dict = json.load(infile)
            infile.close()

        # check if provided vaules are correct
        if email == new_dict['email'] and password == new_dict['password']:
            print('access granted!')
            user_logged_in = True
            # return render_template("logged_in.html")

    return render_template("popular.html",
                           movies=movie_dict['results'],
                           img_path=img_path,
                           img_size=img_size,
                           backdrop_size=backdrop_size
                           )


@app.route("/movies")
def movies():
    return render_template("movies.html")


# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         print('posted')
#         data = request.form
#         with open('static/data/users_info.json', 'w') as f:
#             json.dump(data, f)
#     print('not posted anything')
#     return render_template('thank_you.html')


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     read from users_info.json and
#
#     check if email and pw are correct
#     if email == email & password == password:
#         user_logged_in = True
#     return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
