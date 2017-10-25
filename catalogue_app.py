from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# read .json movies
with open('static/data/popular_movies.json') as in_file:
    movie_dict = json.load(in_file)
    in_file.close()

img_path = 'http://image.tmdb.org/t/p/'
img_size = ["w92", "w154", "w185", "w342", "w500", "w780", "original"]
backdrop_size = ["w300", "w780", "w1280", "original"]


@app.route("/popular", methods=['GET', 'POST'])
def popular():

    # if if request.method == 'POST' and "reg_email" in request.form:

        # read .json users
    with open('static/data/users_info.json') as in_file:
        user_dict = json.load(in_file)
        in_file.close()

    if request.method == 'POST' and "reg_email" in request.form:

        # check if local file corresponds with the provided form values
        if request.form['reg_email'] in user_dict:
            current_user = request.form['reg_email']
            print(current_user)
            print("the email is in the dict")
            if request.form['reg_password'] == str(user_dict[current_user]['password']):
                return render_template("popular.html",
                                       movies=movie_dict['results'],
                                       img_path=img_path,
                                       img_size=img_size,
                                       backdrop_size=backdrop_size)

        # compare the user_dict with the POST'ed form
        posted_form = request.form
        if user_dict[posted_form['email']].user_name == posted_form['email']:
            print('Access Granted!')
            return render_template("thank_you.html")

    elif request.method == 'POST':  # if POST / Signup

        # append
        user_dict[request.form['email']] = request.form

        # write .json users
        with open('static/data/users_info.json', 'w') as outfile:
            json.dump(user_dict, outfile)

        # return thank you
        return render_template('thank_you.html')

    # if no POST, then return popular
    return render_template("popular.html",
                           movies=movie_dict['results'],
                           img_path=img_path,
                           img_size=img_size,
                           backdrop_size=backdrop_size
                           )


@app.route("/<current_movie>")
def movies(current_movie=None):
    # render current movie template
    return render_template("movies.html",
                           current_movie=current_movie,
                           movies=movie_dict['results'],
                           img_path=img_path,
                           img_size=img_size,
                           backdrop_size=backdrop_size
                           )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
