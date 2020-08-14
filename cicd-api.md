#### 1. Creating the infrastructure in the target account
Create the following resources in the target account
- A [cross-account role](https://github.com/awslabs/serverless-api-cross-account-cicd/blob/master/cloudformation/target-account/cf-CrossAccountRole.yml) that has a trust relationship with the tools account. This role provides necessary permissions to CodeBuild in the tools account to carry out deployment.
- An [AWS CloudFormation execution IAM role](https://github.com/awslabs/serverless-api-cross-account-cicd/blob/master/cloudformation/target-account/cf-CloudFormationExecutionRole.yml) that has permissions to create CloudFormation stack resources for your API.

#### 2. Creating the CI/CD pipeline in the tools account

#### 3. Deploying the API


#### 4. Cleanup
