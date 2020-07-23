#!/bin/bash

POSITIONAL=()
while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    -e|--env)
    ENVIRONMENT="$2"
    shift # past argument
    shift # past value
    ;;
    -f|--folder)
    FOLDER="$2"
    shift # past argument
    shift # past value
    ;;
    -n|--name)
	NAME="$2"
	shift
	shift
	;;
    *)    # unknown option
    POSITIONAL+=("$1") # save it in an array for later
    shift # past argument
    ;;
esac
done
set -- "${POSITIONAL[@]}" # restore positional parameters

if [ "${ENVIRONMENT}" = golang ]
then
	cd "golang"
	cd "${FOLDER}"
	GOOS=linux go build main.go
	zip function.zip main
	if [ "$1" = launch ]
	then
		aws lambda create-function --function-name "${NAME}" --runtime go1.x --zip-file fileb://function.zip --handler main --role arn:aws:iam::180390500254:role/lambda_default
	fi
	if [ "$1" = update ]
	then
		aws lambda update-function-code --function-name "${NAME}" --zip-file fileb://function.zip
	fi
fi

if [ "${ENVIRONMENT}" = python ]
then
	cd "python"
	cd "${FOLDER}"
	zip function.zip 
fi
# echo "Environment  = ${ENVIRONMENT}"
# echo "Folder     = ${FOLDER}"
# cd "${FOLDER}"
# echo $(ls)
# echo "$1"
# echo "LIBRARY PATH    = ${LIBPATH}"
# echo "DEFAULT         = ${DEFAULT}"
# echo "Number files in SEARCH PATH with EXTENSION:" $(ls -1 "${SEARCHPATH}"/*."${EXTENSION}" | wc -l)
# if [[ -n $1 ]]; then
    # echo "Last line of file specified as non-opt/last argument:"
    # tail -1 "$1"
# fi


#GOOS=linux go build main.go
#zip function.zip main
#aws lambda create-function --function-name test --runtime go1.x --zip-file fileb://function.zip --handler main --role arn:aws:iam::180390500254:role/lambda_default