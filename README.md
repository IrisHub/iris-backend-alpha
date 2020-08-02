# Iris-Backend-Alpha
Backend scripts for the alpha launch of Iris on July 22nd, 2020

Each lambda function is contained in an individual folder within the "golang" and "python" subdirectories, depending on the environment of the function.

In order to edit a lambda function, edit the source code directly. Once the source code has been edited, upload to AWS Lambda with 
`sh lambda.sh -e ENVIRONMENT -f FUNCTION_FOLDER -n FUNCTION_NAME -p PERMISSION update`.

If you are uploading a new lambda function, upload to AWS Lambda with 
`sh lambda.sh -e ENVIRONMENT -f FUNCTION_FOLDER -n FUNCTION_NAME -p PERMISSION launch`.

# Keyword Arguments in Launch Script
The launch shell script for updating and launching these functions have several required keyword arguments. 

ENVIRONMENT can be either "golang" (`go1.x`) or "python" (`python 3.8.x`). 

The FUNCTION_FOLDER argument is the snake-case folder which contains the function and its associated files.

The  FUNCTION_NAME argument should be the PascalCase equivalent of the FUNCTION_FOLDER keyword.

PERMISSION should be the internal permissions code required for the particular function (i.e. S3 access, DynamoDB access, etc.). A full list of permissions can be found on Notion (TODO).


# How to add features and bugfixes
For any new feature, create a new branch with title 
`<author-name>_feature_<feature-name>`. 
For a bug fix, create a new branch with title 
`<author-name>_bugfix_<bugfix-name>`. 
For any other standard update, create a new branch with title 
`<author-name>_update_<update-name>`.
