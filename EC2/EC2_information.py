import boto3
ec2client = boto3.client('ec2',region_name='eu-north-1')
response = ec2client.describe_instances()
for reservation in response.get('Reservations'):
    for instance in reservation.get('Instances'):
        print(instance["InstanceId"])