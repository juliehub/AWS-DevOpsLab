### 1. Creating the infrastructure in the target account
Create the following resources in the target account
#### 1.1 A cross-account role that has a trust relationship with the tools account
This role provides necessary permissions to CodeBuild in the tools account to carry out deployment.

- On the AWS CloudFormation console, choose `Create stack`.
- Upload a [template](https://github.com/awslabs/serverless-api-cross-account-cicd/blob/master/cloudformation/target-account/cf-CrossAccountRole.yml) to Amazon S3.
- Enter stack name `myapp-cicd-pipeline-CrossAccountRole` and specify your designated AWS account ID for the tools account in the `ToolsAccountID` parameter.
- Select `I acknowledge that AWS CloudFormation might create IAM resources with custom names.` and click `Create`
#### 1.2 An AWS CloudFormation execution IAM role that has permissions to create CloudFormation stack resources for your API
- On the AWS CloudFormation console, choose `Create stack`.
- Upload a [template](https://github.com/awslabs/serverless-api-cross-account-cicd/blob/master/cloudformation/target-account/cf-CloudFormationExecutionRole.yml)
- Select `I acknowledge that AWS CloudFormation might create IAM resources with custom names.` and click `Create`

### 2. Creating the CI/CD pipeline in the tools account

### 3. Deploying the API


### 4. Cleanup
