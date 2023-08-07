#!/bin/sh

#cf. https://gist.github.com/SheldonWangRJT/8d3f44a35c8d1386a396b9b49b43c385

input_file=$1
filename=$(basename -- "${input_file%.*}")
ffmpeg -i ${input_file} -pix_fmt rgb8 -r 1 ${filename}.gif && gifsicle -O3 ${filename}.gif -o ${filename}.gif && echo "Video ${filename} is ready."
