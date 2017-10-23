import json

movie_img_list = []
backdrop_img_list = []

# read from .json
with open('static/data/popular_movies.json') as in_file:
    movie_dict = json.load(in_file)
    in_file.close()

for movie in movie_dict['results']:
    movie_img_list.append(movie['poster_path'])
    backdrop_img_list.append(movie['backdrop_path'])

print(movie_img_list)
print(backdrop_img_list)

# write to extruded_img_list.txt
with open('static/data/extruded_img_list.txt', 'w') as outfile:
    for movie in movie_img_list:
        outfile.write(movie + '\n')
