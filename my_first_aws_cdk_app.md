### Prerequisites
- Install [Node.js 10.3.0](https://nodejs.org/en/download/) or later
- Install the AWS CLI and issue the following command `aws configure`
- Install Python 3.6 or later including `pip` and `virtualenv`
- Install the AWS CDK `npm install -g aws-cdk` and verify by running command `cdk --version`
- Install the [AWS Toolkit for Visual Studio Code](https://aws.amazon.com/visualstudiocode/) is an open-source plug-in for Visual Studio Code
- Install the [AWS CDK Explorer feature](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/setup-toolkit.html) to list your AWS CDK projects and browse the various components of the CDK application

### Hello-World App
#### 1. Create the app
Create a new directory for your app
```bash
$ mkdir hello-cdk
$ cd hello-cdk
```
Initialize the app using the cdk init command, specifying the desired template ("app") and programming language
```bash
$ cdk init app --language python
Applying project template app for python

# Welcome to your CDK Python project!

This is a blank project for Python development with CDK.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the .env
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

`$ python -m venv .env`

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

`$ source .env/bin/activate`

If you are a Windows platform, you would activate the virtualenv like this:

`% .env\Scripts\activate.bat`

Once the virtualenv is activated, you can install the required dependencies.

`
$ pip install -r requirements.txt
`

At this point you can now synthesize the CloudFormation template for this code.

`
$ cdk synth
`

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!

Initializing a new git repository...
warning: LF will be replaced by CRLF in .gitignore.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in README.md.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in app.py.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in cdk.json.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in hello_cdk/hello_cdk_stack.py.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in requirements.txt.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in setup.py.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in source.bat.
The file will have its original line endings in your working directory
Please run python -m venv .env'!
Executing Creating virtualenv...
✅ All done!

```

After the app has been created, also enter the following two commands to activate
the app's Python virtual environment and install its dependencies.
```bash
C:\Users\julie\hello-cdk>source .env/bin/activate
Executing .env\Scripts\activate.bat for you
(.env) C:\Users\julie\hello-cdk>python -m pip install -r requirements.txt
Obtaining file:///C:/Users/julie/hello-cdk (from -r requirements.txt (line 1))
Collecting aws-cdk.core==1.60.0
  Downloading aws_cdk.core-1.60.0-py3-none-any.whl (1.0 MB)
     |████████████████████████████████| 1.0 MB 1.6 MB/s
Collecting aws-cdk.cx-api==1.60.0
  Downloading aws_cdk.cx_api-1.60.0-py3-none-any.whl (118 kB)
     |████████████████████████████████| 118 kB 1.7 MB/s
Collecting publication>=0.0.3
  Downloading publication-0.0.3-py2.py3-none-any.whl (7.7 kB)
Collecting constructs<4.0.0,>=3.0.2
  Downloading constructs-3.0.4-py3-none-any.whl (76 kB)
     |████████████████████████████████| 76 kB 383 kB/s
Collecting aws-cdk.cloud-assembly-schema==1.60.0
  Downloading aws_cdk.cloud_assembly_schema-1.60.0-py3-none-any.whl (116 kB)
     |████████████████████████████████| 116 kB 2.2 MB/s
Collecting jsii<2.0.0,>=1.9.0
  Downloading jsii-1.11.0-py3-none-any.whl (266 kB)
     |████████████████████████████████| 266 kB 2.2 MB/s
Collecting typing-extensions~=3.7.4
  Downloading typing_extensions-3.7.4.3-py3-none-any.whl (22 kB)
Collecting attrs~=19.3.0
  Using cached attrs-19.3.0-py2.py3-none-any.whl (39 kB)
Collecting python-dateutil
  Downloading python_dateutil-2.8.1-py2.py3-none-any.whl (227 kB)
     |████████████████████████████████| 227 kB 1.6 MB/s
Collecting cattrs~=1.0.0
  Downloading cattrs-1.0.0-py2.py3-none-any.whl (14 kB)
Collecting six>=1.5
  Downloading six-1.15.0-py2.py3-none-any.whl (10 kB)
Installing collected packages: typing-extensions, attrs, six, python-dateutil, cattrs, jsii, publication, aws-cdk.cloud-assembly-schema, aws-cdk.cx-api, constructs, aws-cdk.core, hello-cdk
  Running setup.py develop for hello-cdk
Successfully installed attrs-19.3.0 aws-cdk.cloud-assembly-schema-1.60.0 aws-cdk.core-1.60.0 aws-cdk.cx-api-1.60.0 cattrs-1.0.0 constructs-3.0.4 hello-cdk jsii-1.11.0 publication-0.0.3 python-dateutil-2.8.1 six-1.15.0 typing-extensions-3.7.4.3
```
List the stacks in the app
```bash
(.env) C:\Users\julie\hello-cdk>cdk ls
hello-cdk
```
#### 2. Add an Amazon S3 bucket
Install the Amazon S3 package from the AWS Construct Library.
```bash
(.env) C:\Users\julie\hello-cdk>pip install aws-cdk.aws-s3
Collecting aws-cdk.aws-s3
  Downloading aws_cdk.aws_s3-1.60.0-py3-none-any.whl (284 kB)
     |████████████████████████████████| 284 kB 1.3 MB/s
Collecting aws-cdk.aws-iam==1.60.0
  Downloading aws_cdk.aws_iam-1.60.0-py3-none-any.whl (359 kB)
     |████████████████████████████████| 359 kB 2.2 MB/s
Collecting aws-cdk.aws-kms==1.60.0
  Downloading aws_cdk.aws_kms-1.60.0-py3-none-any.whl (79 kB)
     |████████████████████████████████| 79 kB 891 kB/s
Requirement already satisfied: aws-cdk.core==1.60.0 in c:\users\julie\hello-cdk\.env\lib\site-packages (from aws-cdk.aws-s3) (1.60.0)
Collecting aws-cdk.aws-events==1.60.0
  Downloading aws_cdk.aws_events-1.60.0-py3-none-any.whl (141 kB)
     |████████████████████████████████| 141 kB 1.6 MB/s
Requirement already satisfied: jsii<2.0.0,>=1.9.0 in c:\users\julie\hello-cdk\.env\lib\site-packages (from aws-cdk.aws-s3) (1.11.0)
Requirement already satisfied: constructs<4.0.0,>=3.0.2 in c:\users\julie\hello-cdk\.env\lib\site-packages (from aws-cdk.aws-s3) (3.0.4)
Requirement already satisfied: publication>=0.0.3 in c:\users\julie\hello-cdk\.env\lib\site-packages (from aws-cdk.aws-s3) (0.0.3)
Collecting aws-cdk.region-info==1.60.0
  Downloading aws_cdk.region_info-1.60.0-py3-none-any.whl (63 kB)
     |████████████████████████████████| 63 kB 206 kB/s
Requirement already satisfied: aws-cdk.cx-api==1.60.0 in c:\users\julie\hello-cdk\.env\lib\site-packages (from aws-cdk.core==1.60.0->aws-cdk.aws-s3) (1.60.0)
Requirement already satisfied: aws-cdk.cloud-assembly-schema==1.60.0 in c:\users\julie\hello-cdk\.env\lib\site-packages (from aws-cdk.core==1.60.0->aws-cdk.aws-s3) (1.60.0)
Requirement already satisfied: cattrs~=1.0.0 in c:\users\julie\hello-cdk\.env\lib\site-packages (from jsii<2.0.0,>=1.9.0->aws-cdk.aws-s3) (1.0.0)
Requirement already satisfied: typing-extensions~=3.7.4 in c:\users\julie\hello-cdk\.env\lib\site-packages (from jsii<2.0.0,>=1.9.0->aws-cdk.aws-s3) (3.7.4.3)
Requirement already satisfied: python-dateutil in c:\users\julie\hello-cdk\.env\lib\site-packages (from jsii<2.0.0,>=1.9.0->aws-cdk.aws-s3) (2.8.1)
Requirement already satisfied: attrs~=19.3.0 in c:\users\julie\hello-cdk\.env\lib\site-packages (from jsii<2.0.0,>=1.9.0->aws-cdk.aws-s3) (19.3.0)
Requirement already satisfied: six>=1.5 in c:\users\julie\hello-cdk\.env\lib\site-packages (from python-dateutil->jsii<2.0.0,>=1.9.0->aws-cdk.aws-s3) (1.15.0)
Installing collected packages: aws-cdk.region-info, aws-cdk.aws-iam, aws-cdk.aws-kms, aws-cdk.aws-events, aws-cdk.aws-s3
Successfully installed aws-cdk.aws-events-1.60.0 aws-cdk.aws-iam-1.60.0 aws-cdk.aws-kms-1.60.0 aws-cdk.aws-s3-1.60.0 aws-cdk.region-info-1.60.0
```
Next, define an Amazon S3 bucket in the stack using an L2 construct, the Bucket class.
Update `hello_cdk/hello_cdk_stack.py` with the [following code](https://github.com/juliehub/AWS-DevOpsLab/blob/master/hello-cdk_stack.py)
#### 3. Synthesize an AWS CloudFormation template
Sample CloudFormation file [hello-cdk.yaml](https://github.com/juliehub/AWS-DevOpsLab/blob/master/hello-cdk.yaml)
```bash
(.env) C:\Users\julie\hello-cdk>cdk synth
Resources:
  MyFirstBucketjulie69D277EB:
    Type: AWS::S3::Bucket
    Properties:
      VersioningConfiguration:
        Status: Enabled
    UpdateReplacePolicy: Retain
    DeletionPolicy: Retain
    Metadata:
      aws:cdk:path: hello-cdk/MyFirstBucket-julie/Resource
  CDKMetadata:
    Type: AWS::CDK::Metadata
    Properties:
      Modules: aws-cdk=1.60.0,@aws-cdk/aws-events=1.60.0,@aws-cdk/aws-iam=1.60.0,@aws-cdk/aws-kms=1.60.0,@aws-cdk/aws-s3=1.60.0,@aws-cdk/cloud-assembly-schema=1.60.0,@aws-cdk/core=1.60.0,@aws-cdk/cx-api=1.60.0,@aws-cdk/region-info=1.60.0,jsii-runtime=Python/3.8.5
    Condition: CDKMetadataAvailable
....
```
#### 5. Deploying the stack
```bash
(.env) C:\Users\julie\hello-cdk>cdk deploy
hello-cdk: deploying...
hello-cdk: creating CloudFormation changeset...
 0/3 | 4:30:43 PM | REVIEW_IN_PROGRESS   | AWS::CloudFormation::Stack | hello-cdk User Initiated
 0/3 | 4:30:49 PM | CREATE_IN_PROGRESS   | AWS::CloudFormation::Stack | hello-cdk User Initiated
 0/3 | 4:30:52 PM | CREATE_IN_PROGRESS   | AWS::CDK::Metadata | CDKMetadata
 0/3 | 4:30:52 PM | CREATE_IN_PROGRESS   | AWS::S3::Bucket    | MyFirstBucket-julie (MyFirstBucketjulie69D277EB)
 1/3 | 4:30:54 PM | CREATE_IN_PROGRESS   | AWS::CDK::Metadata | CDKMetadata Resource creation Initiated
 1/3 | 4:30:54 PM | CREATE_COMPLETE      | AWS::CDK::Metadata | CDKMetadata
 1/3 | 4:30:54 PM | CREATE_IN_PROGRESS   | AWS::S3::Bucket    | MyFirstBucket-julie (MyFirstBucketjulie69D277EB) Resource creation Initiated
 3/3 | 4:31:15 PM | CREATE_COMPLETE      | AWS::S3::Bucket    | MyFirstBucket-julie (MyFirstBucketjulie69D277EB)
 3/3 | 4:31:16 PM | CREATE_COMPLETE      | AWS::CloudFormation::Stack | hello-cdk

 ✅  hello-cdk

Stack ARN:
arn:aws:cloudformation:ap-southeast-2:<acccountID>:stack/hello-cdk/ab0adb30-e765-11ea-bb05-06bea7b10744
```
You can go to the AWS CloudFormation console and see that it now lists HelloCdkStack. You'll also find MyFirstBucket in the Amazon S3 console.
#### 6. Modifying the app
Update `hello_cdk/hello_cdk_stack.py`
We want to be able to delete the bucket automatically when we delete the stack, so we'll change the RemovalPolicy.
```python
bucket = s3.Bucket(self, 
        "MyFirstBucket-julie", 
         versioned=True,
         removal_policy=core.RemovalPolicy.DESTROY)
```
The AWS CDK Toolkit queries your AWS account for the current AWS CloudFormation template for the hello-cdk stack,
and compares it with the template it synthesized from your app.
```bash
(.env) C:\Users\julie\hello-cdk>cdk diff
Stack hello-cdk
Resources
[~] AWS::S3::Bucket MyFirstBucket-julie MyFirstBucketjulie69D277EB
 ├─ [~] DeletionPolicy
 │   ├─ [-] Retain
 │   └─ [+] Delete
 └─ [~] UpdateReplacePolicy
     ├─ [-] Retain
     └─ [+] Delete
```
Deploy stack
```bash
cdk deploy
hello-cdk: deploying...
hello-cdk: creating CloudFormation changeset...
   1 | 5:14:15 PM | UPDATE_IN_PROGRESS   | AWS::CloudFormation::Stack | hello-cdk User Initiated
   1 | 5:14:20 PM | UPDATE_COMPLETE      | AWS::S3::Bucket    | MyFirstBucket-julie (MyFirstBucketjulie69D277EB)
   2 | 5:14:22 PM | UPDATE_COMPLETE_CLEA | AWS::CloudFormation::Stack | hello-cdk
   2 | 5:14:22 PM | UPDATE_COMPLETE      | AWS::CloudFormation::Stack | hello-cdk

 ✅  hello-cdk

Stack ARN:
arn:aws:cloudformation:ap-southeast-2:<accountID>:stack/hello-cdk/ab0adb30-e765-11ea-bb05-06bea7b10744
```
#### 7. Destroying the app's resources
```bash
(.env) C:\Users\julie\hello-cdk>cdk destroy
Are you sure you want to delete: hello-cdk (y/n)? y
hello-cdk: destroying...

 ✅  hello-cdk: destroyed
```
