#!/usr/bin/env bash

# package the Lambda function, including necessary libraries
zip -r ggcstatus.zip ggcstatus.py greengrasssdk/ greengrass_common/ greengrass_ipc_python_sdk

# update function code in AWS (you must configure your environment properly to use awscli
# tested with aws-cli/1.15.3 Python/3.7.0a2 Darwin/17.5.0 botocore/1.10.3

# specify profile as appropriate in ~/.aws/credentials; youre user must have permissions to update function code in Lambda
aws --profile ccdtw lambda update-function-code --function-name ggcstatus --zip-file fileb://ggcstatus.zip --region us-east-1


