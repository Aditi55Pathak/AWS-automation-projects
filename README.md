# AWS Automation with Python Boto3 and Lambda Functions

## [PART - 1] Introduction

### Aim
Learn how to automate AWS common tasks using Boto3 and Lambda Functions.

### Objectives
1. Cover the core concepts of Boto3 and Lambda.
2. Understand Boto3 and Lambda concepts with real-time scenarios.
3. Run Boto3 scripts on your local machine and trigger Lambda functions.
4. Gain the knowledge to apply different concepts of Boto3 and Lambda for various AWS Services.

### Pre-requisites
What do you need for this course?
1. AWS Account - A free tier account is recommended.
2. Basic knowledge of AWS Services and Python (optional).
3. Familiarity with any Python IDE (optional).

**Note**: All the videos will be uploaded to the “AWS Automation with Python Boto3” playlist.

## [PART - 2] Introduction to Boto3

### What is Boto3?
- Boto3 is the Python SDK/Library/Module/API for AWS.
- It allows direct creation, updating, and deletion of AWS services from Python scripts.
- Boto3 is built on top of the botocore module.

### Installing Boto3

#### On Windows Machine
1. Install Python-3.7.4 from [python.org](https://www.python.org)
2. Set paths for Python and pip3
3. Install Boto3 using `pip3 install boto3`

#### On Linux Machine
```bash
yum install gcc openssl-devel bzip2-devel libffi-devel
cd /usr/src
wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz
tar xzf Python-3.7.4.tgz
cd Python-3.7.4
./configure --enable-optimizations
make altinstall
cd /usr/local/bin/
./python3.7 --version
./pip3.7 --version
ln -s /usr/local/bin/python3.7 /bin/python3
python3 --version
ln -s /usr/local/bin/pip3.7 /bin/pip3
pip3 --version
pip3 install boto3
```

## [PART 3] Boto3 Environment Setup

### Configure AWS CLI
The AWS Command Line Interface (AWS CLI) is a unified tool to manage your AWS services. It allows you to control multiple AWS services from the command line and automate them through scripts.

1. Download and install AWS CLI: [AWS CLI Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
2. Log in to AWS Management Console and create a new user with programmatic access and provide `AdministratorAccess`.
3. Configure root/IAM user access-keys/credentials using:
   ```bash
   aws configure
   ```
   OR use different profiles for different environments:
   ```bash
   aws configure --profile dev
   aws configure --profile qa
   aws configure --profile prod
   ```

### First Automation Script
List all the IAM users in your account.

#### Manual Steps
1. Access AWS Management Console: [AWS Console](https://aws.amazon.com/console/)
2. Go to IAM Console and explore options like Users, Groups, Roles, Policies, etc.

**Link to the code**: [Boto3 Course Project](https://github.com/yeshwanthlm/Boto3-Course-YouTube/tree/main/Project-1)

## [PART 4] Concepts of Boto3

### Key Concepts
- **Session**: Manages configurations and credentials, allowing creation of service clients and resources.
- **Resource**: Higher-level, object-oriented service access (available for selected services).
- **Client**: Low-level service access with dictionary responses.
- **Meta**: Allows transitioning between Resource and Client.
- **Collections**: Group of related resources.
- **Waiters**: Automates waiting for resource states.
- **Paginators**: Handles paginated responses from AWS services.

### Session
- Stores configuration information and allows creation of service clients and resources.
- Default session is created when needed, but multiple sessions can be created in the same script.

![image](https://github.com/Aditi55Pathak/AWS-automation-projects/assets/80877301/fe032ce7-3377-4e31-9267-6e7cc66b0b54)

![image](https://github.com/Aditi55Pathak/AWS-automation-projects/assets/80877301/e5353dcc-b628-4723-8e83-60fa2cd2d0f0)



### Resource and Client
- Resource provides higher-level object-oriented access.
- Client offers low-level service access with dictionary responses.
- Resource is available for selected services: ['cloudformation', 'cloudwatch', 'dynamodb', 'ec2', 'glacier', 'iam', 'opsworks', 's3', 'sns', 'sqs'].

![image](https://github.com/Aditi55Pathak/AWS-automation-projects/assets/80877301/6940f272-91fe-4fc0-a98f-9489fe196440)

Example for Resource Object:

![image](https://github.com/Aditi55Pathak/AWS-automation-projects/assets/80877301/683c1cc0-1557-4796-9a5d-fe65d2f09ff5)

Example for Client Object:

![image](https://github.com/Aditi55Pathak/AWS-automation-projects/assets/80877301/bfbed287-cf42-4af8-83ad-a664145bfc34)


Should I choose Resource or Client? 🤔

●	You can choose anyone depending on your use case.
●	Resource is Higher Level Object oriented service access. 
●	Resource objects are only available for a few AWS Services.
●	Let us check which AWS Service has a Resource Object!!!  - DEM😉
●	['cloudformation', 'cloudwatch', 'dynamodb', 'ec2', 'glacier', 'iam', 'opsworks', 's3', 'sns', 'sqs'] - Resource Object Available.
●	Client is Low Level Service Access.
●	In simple terms, the output/response in case of Client will be in Dictionary, which needs more effort in implementing boto3 scripts.
●	Whereas Resource is an object, we can use simple (.) operation.
●	All operations that we see in AWS Management Console can be done in Client whereas Resource does not guarantee you that. Some operations may not be supported.
●	If we do not have some operations in Resource we can enter into Client by using the “Meta” concept. Let us talk about this later! 😉
●	Let us see how much effort is needed for both Resource and Client. - DEM😀



## [PART 5] Boto3 Script with Documentation (Demo)

### Example Scripts
1. List all IAM users using client objects.
2. List all running EC2 instances using client objects.
3. List all IAM users using resource objects.
4. List all running EC2 instances using resource objects.

By following this guide, you will learn to automate AWS tasks using Boto3 and Lambda functions, applying the concepts to various AWS services efficiently.
