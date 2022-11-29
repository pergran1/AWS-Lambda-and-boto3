import os
import boto3

ec2 = boto3.resource('ec2')


# WHen using lambda in AWS dont forget to add role to the function

def create_ec2():
    instance = ec2.create_instances(
        ImageId='ami-02aeff1a953c5c2ff',
        InstanceType='t3.micro',
        KeyName='lambdaEC2keyPair',
        SubnetId='subnet-0ca596c43c463291e',
        MaxCount=1,
        MinCount=1
    )

    print("New insteance created:", instance[0].id)


create_ec2()
