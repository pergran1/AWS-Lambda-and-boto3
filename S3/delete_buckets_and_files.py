from typing import List, Dict, Any
import boto3
import logging
import datetime

logging.basicConfig(filename="log.txt", level=logging.INFO, force=True)
from S3.search_buckets import bucket_list, get_buckets_time_creation


def delete_by_name(bucket_name: str) -> None:
    s3 = boto3.client('s3')
    objects = s3.list_objects_v2(Bucket=bucket_name)
    nbr_of_objects: int = objects.get('KeyCount')  # must be 0 objects in bucket
    if nbr_of_objects == 0:
        # Delete the bucket
        s3.delete_bucket(Bucket=bucket_name)
        logging.info(f"The bucket: {bucket_name} was deleted {datetime.datetime.now()} ")


def delete_by_time(start_time, end_time):
    """
    Function to delete buckets that are created in a specific time period
    :param start_time:
    :param end_time:

    """
    bucket_dict = get_buckets_time_creation()
    for bucket in bucket_dict:
        if start_time <= bucket.get('CreationDate') <= end_time:
            print(
                f"{bucket.get('CreationDate')} is {bucket.get('CreationDate') >= end_time}  the end_time is {end_time}")


delete_by_time('2022-06-01', '2022-08-01')
