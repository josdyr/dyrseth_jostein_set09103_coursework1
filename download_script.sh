#!/bin/sh

i=0
while read p; do
  echo $p
  curl 'http://image.tmdb.org/t/p/original'$p -o 'static/popular/movie_images/movie_img'$i'.png'
  i=$((i+1))
done < extruded_img_list.txt

j=0
while read p; do
  echo $p
  curl 'http://image.tmdb.org/t/p/original'$p -o 'static/popular/cover_images/cover_img'$j'.png'
  j=$((j+1))
done < extruded_cover_list.txt

exit
