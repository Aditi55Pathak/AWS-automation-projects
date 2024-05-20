# Import necessary modules
import boto3

# open management console
aws_mgmt_console=boto3.session.Session(profile_name="default")

# open ec2 console
ec2_console=aws_mgmt_console.client(service_name='ec2')

#  implementing 

result=ec2_console.describe_instances()['Reservations']
print(result)


