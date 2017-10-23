#!/bin/sh

i=0

while read p; do
  echo $p
  curl 'http://image.tmdb.org/t/p/original'$p -o 'folder_img/movie_img'$i'.png'
  i=$((i+1))
done < extruded_img_list.txt

exit
