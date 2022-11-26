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
    return [s3.get_bucket_location(Bucket=bucket_name).get('LocationConstraint') for bucket_name in bucket_names]


def get_bucket_info() -> None:
    """
    Will provide information for each bucket such as:
    Name, created, region, last changed, nbr of folder, number of files
    """
    bucket_names: List[str] = get_bucket_names()
    regions: List[str] = get_bucket_locations()

    for name, region in zip(bucket_names, regions):
        bucket_info_dict = get_bucket_objects(name)
        print(f"Bucketname: {name} region: {region} nbr of folders: {bucket_info_dict.get('nbr_folders')}"
              f" nbr of files: {bucket_info_dict.get('nbr_files')}")


def get_bucket_objects(bucket_name: str) -> dict:
    info_dict = {'nbr_folders': 0, 'nbr_files': 0}
    s3 = boto3.client('s3')
    response: List[dict] = s3.list_objects(Bucket=bucket_name)
    # print(response.get('Contents'))
    response_list = response.get('Contents')
    if (response_list == None):
        return info_dict
    for key in response_list:
        keys = key.get('Key')
        try:
            if len(keys.split('/')[1]) == 0:
                info_dict["nbr_folders"] += 1
            else:
                info_dict['nbr_files'] += 1
        except:
            continue
    return info_dict


get_bucket_info()

