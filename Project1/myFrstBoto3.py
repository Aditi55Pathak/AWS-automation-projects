import boto3
import boto3.session

aws_management_console=boto3.session.Session(profile_name="default")
iam_console=aws_management_console.resource('iam')

for each_user in iam_console.users.all():
    print(each_user.name)

# Important key Concepts

    # Session: Managing AWS console programmatically

    # Resource : Resource is a high level object oriented service access
    #           It is used to access the AWS services

