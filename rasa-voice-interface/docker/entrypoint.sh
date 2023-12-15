#!/bin/sh

ROOT_DIR=/usr/share/nginx/html

echo "Replacing env constants in JS"
for file in $ROOT_DIR/assets/js/app.js $ROOT_DIR/index.html;
do
  echo "Processing $file ...";

  sed -i 's|VUE_RASA_APP_PUBLIC_URL|'${VUE_RASA_APP_PUBLIC_URL}'|g' $file

done

echo "Starting Nginx"
nginx -g 'daemon off;'
