"""
This code creates a bucket where the user specifies the bucket name and region.

If the bucket already exist than it will create a new bucket with the same name but with a number at the end.

Example: Original name = this-bucket-already-exist
The new bucket when the function runs again: this-bucket-already-exist-1

"""
import json
import boto3

s3 = boto3.client('s3')
bucket_name: str = 'created-by-lambda-testing-swe'
region: str = 'eu-north-1'


def create_bucket(bucket_name: str = bucket_name, region: str = region ):
    s3.create_bucket(Bucket=bucket_name,
                     CreateBucketConfiguration={
                         'LocationConstraint': region,
                     },
                     )


def lambda_handler(event, context):
    created_bucket: bool = False
    tried_buckets: int = 0
    while created_bucket == False:
        try:
            tried_buckets += 1
            create_bucket()
            created_bucket = True

        except:
            create_bucket(f"{bucket_name}-{tried_buckets}")
            created_bucket = True
