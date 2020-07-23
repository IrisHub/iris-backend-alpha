# Iris-Backend-Alpha
Backend scripts for the alpha launch of Iris on July 22nd, 2020

Each lambda function is contained in an individual folder within the "golang" and "python" subdirectories, depending on the environment of the function.

In order to edit a lambda function, edit the source code directly. Once the source code has been edited, upload to AWS Lambda with 
`sh lambda.sh -e ENVIRONMENT -f FUNCTION_FOLDER -n FUNCTION_NAME update`.

If you are uploading a new lambda function, upload to AWS Lambda with 
`sh lambda.sh -e ENVIRONMENT -f FUNCTION_FOLDER -n FUNCTION_NAME launch`.


# How to add features and bugfixes
For any new feature, create a new branch with title 
`<author-name>_feature_<feature-name>`. 
For a bug fix, create a new branch with title 
`<author-name>_bugfix_<bugfix-name>`. 
For any other standard update, create a new branch with title 
`<author-name>_update_<update-name>`.
