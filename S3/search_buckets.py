from typing import List, Dict, Any

import boto3


def bucket_list() -> List[dict]:
    s3 = boto3.client('s3')
    bucket_dic = s3.list_buckets()
    buckets: List[dict] = bucket_dic['Buckets']
    return buckets


def get_bucket_names() -> List[str]:
    bucket_dic: List[Dict[Any, Any]] = bucket_list()
    return [s3_name['Name'] for s3_name in bucket_dic]


def get_bucket_locations() -> List[str]:
    s3 = boto3.client('s3')
    bucket_names: List[str] = get_bucket_names()
    return [s3.get_bucket_location(Bucket=bucket_name)['LocationConstraint'] for bucket_name in bucket_names]


def get_bucket_info() -> None:
    """
    Will provide information for each bucket such as:
    Name, created, region, last changed, nbr of folder, number of files
    """
    bucket_names: List[str] = get_bucket_names()
    regions: List[str] = get_bucket_locations()

    for name, region in zip(bucket_names, regions):
        print(f"Bucketname: {name} region: {region}")


print(get_bucket_names())
print(get_bucket_locations())
get_bucket_info()
