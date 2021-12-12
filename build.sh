#!/bin/bash 
# This builds the layer

set -e


NAME="$1"

FILE="${NAME}/Dockerfile"
if ! [ -f "$FILE" ]; then
    echo "'$FILE' DOES NOT EXIST!"
    echo "Enter the name of the folder you want to use: for example:"
    echo "./build.sh fuzzywuzzy # builds fuzzywuzzy.zip"
    exit 1
fi



LAYER="pancakes_${NAME}"
ZIPFILE="pancakes_${NAME}.zip"

# Delete any previous version
rm -rf $ZIPFILE

sudo docker build -t $LAYER ${NAME}/
CONTAINER=$(sudo docker run -d $LAYER false)
echo "Copying layer.zip from the docker container"
sudo docker cp ${CONTAINER}:/layer.zip "${ZIPFILE}"
sudo chown -R "${USER}:${USER}" "${ZIPFILE}"
sudo docker container rm  ${CONTAINER}
echo "Created $ZIPFILE"
