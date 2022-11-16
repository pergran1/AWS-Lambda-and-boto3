# This is code that will create S3 bucket and insert a csv
# This code will be used on a lambda function, but it can run in a python local

import boto3

s3 = boto3.client('s3')
s3.create_bucket(Bucket="created_by_lambda",
                 CreateBucketConfiguration={
                     'LocationConstraint': 'eu-north-1',
                 },
                 )
