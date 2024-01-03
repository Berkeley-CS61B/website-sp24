shopt -s nullglob

for i in *.{png,PNG,gif,GIF,heic,HEIC,jpg,JPG,jpeg,JPEG,jfif,JFIF}; do
  input="$i"
  output="${i%.*}.jpg"
    max_dim=$(identify -format "%[fx:max(w,h)]" "$input")
  if [ -z "$max_dim" ]; then
    max_dim=0
  fi
  if [ "$max_dim" -lt 512 ]; then
    max_dim=512
  fi
  sudo convert "$input" -gravity center -background none -resize ${max_dim}x${max_dim}^ -extent ${max_dim}x${max_dim} -strip "$output"
done

shopt -u nullglob