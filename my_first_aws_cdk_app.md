### Prerequisites
- Install [Node.js 10.3.0](https://nodejs.org/en/download/) or later
- Install the AWS CLI and issue the following command `aws configure`
- Install Python 3.6 or later including `pip` and `virtualenv`
- Install the AWS CDK `npm install -g aws-cdk` and verify by running command `cdk --version`
- Install the `AWS Toolkit for Visual Studio Code`(https://aws.amazon.com/visualstudiocode/) is an open-source plug-in for Visual Studio Code
- Install the [AWS CDK Explorer feature](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/setup-toolkit.html) to list your AWS CDK projects and browse the various components of the CDK application

#### Hello-World App
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
