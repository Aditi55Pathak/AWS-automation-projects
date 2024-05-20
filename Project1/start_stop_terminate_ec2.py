import boto3
import boto3.session

aws_management_console = boto3.session.Session(profile_name='default')
ec2_console = aws_management_console.client('ec2')

# response=ec2_console.start_instances()
# response=ec2_console.stop_instances()

response=ec2_console.terminate_instances(
    InstanceIds=['i-000b9e56b80edfee9']
)