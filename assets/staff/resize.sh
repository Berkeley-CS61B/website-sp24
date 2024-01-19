#!/bin/bash

shopt -s nullglob
for i in *.{png,PNG,gif,GIF,heic,HEIC}; do convert "$i" "${i%.*}.jpg"; done
for i in *.{JPG,jpeg,JPEG,jfif,JFIF}; do mv "$i" "${i%.*}.jpg"; done
mogrify -resize '512x512^>' -gravity center -crop '512x512+0+0' -strip *.jpg
shopt -u nullglob