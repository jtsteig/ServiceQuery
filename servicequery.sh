#!/bin/bash

mkdir -p build

####  Constants #####
BUCKETNAME="servicequery-jsteig"
ZIPNAME="ServiceQuery.zip"
##### Functions #####

setup_bucket()
{
  aws s3api create-bucket --bucket $BUCKETNAME --region us-west-1 --create-bucket-configuration LocationConstraint=us-west-1
}

zip_packages()
{
    cd ./src
    zip -FSr ../build/$ZIPNAME *
    SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    if [ -z "$VIRTUAL_ENV_DIR" ]; then
      VIRTUAL_ENV_DIR="$SCRIPT_DIR/venv"
    fi
    echo "Using virtualenv located in : $VIRTUAL_ENV_DIR"
    cd $VIRTUAL_ENV_DIR/lib/python3.6/site-packages
    zip -r9 $SCRIPT_DIR/../build/$ZIPNAME *
    zip -d $SCRIPT_DIR/../build/$ZIPNAME "venv/*"
    cd ..
}

build_to_amazon()
{
  cd ./src  
  aws lambda update-function-code --function-name ServiceQuery --zip-file fileb://../build/$ZIPNAME
 
  cd ..
}

##### Handle  #####
if [ "$1" == "-b" ]
then
  build_to_amazon
  exit
fi
if [ "$1" == "-z" ]
then
    zip_packages
    exit
fi
echo "Invalid parameters."

