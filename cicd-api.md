### 1. Creating the infrastructure in the target account
Create the following resources in the target account
#### 1.1 A cross-account role that has a trust relationship with the tools account
This role provides necessary permissions to CodeBuild in the tools account to carry out deployment.

- On the AWS CloudFormation console, choose `Create stack`.
- Upload a [template](https://github.com/awslabs/serverless-api-cross-account-cicd/blob/master/cloudformation/target-account/cf-CrossAccountRole.yml) to Amazon S3.
- Enter stack name `myapp-cicd-pipeline-CrossAccountRole` and specify your designated AWS account ID for the tools account in the `ToolsAccountID` parameter.
Note that AWS account ID is a 12 digit string (a string with Pattern: \d{12}). [References] (https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html)

- Select `I acknowledge that AWS CloudFormation might create IAM resources with custom names.` and click `Create`

This CloudFormation template will create 2 resources:
- CrossAccountDeploymentRole
- CrossAccountDeploymentPolicy

It returns the following outputs:
| Key | Value | Description |
| --- | --- | --- |
| OutCrossAccountDeploymentPolicy | arn:aws:iam::<TargetAccountID>:policy/cross-account-policy-serverless-deployment | Cross Account Deployment Policy ARN | 
| OutCrossAccountDeploymentRole | arn:aws:iam::<TargetAccountID>:role/cross-account-role-serverless-deployment | Cross Account Deployment Role ARN |

#### 1.2 An AWS CloudFormation execution IAM role that has permissions to create CloudFormation stack resources for your API
- On the AWS CloudFormation console, choose `Create stack`.
- Upload a [template](https://github.com/awslabs/serverless-api-cross-account-cicd/blob/master/cloudformation/target-account/cf-CloudFormationExecutionRole.yml) to Amazon S3.
- Enter stack name `myapp-cicd-pipeline-CloudFormationExecutionRole`
- Select `I acknowledge that AWS CloudFormation might create IAM resources with custom names.` and click `Create`

This CloudFormation template will create 2 resources:
- CFExecutionRole
- CFExecutionPolicy

It returns the following outputs:
| Key | Value | Description |
| --- | --- | --- |
| OutCFExecutionRole | arn:aws:iam::<TargetAccountID>:role/cf-execution-role-serverless | CloudFormation Execution Role ARN |
| OutCrossAccountDeploymentPolicy | arn:aws:iam::<TargetAccountID>:policy/cf-execution-policy-serverless | CloudFormation Execution Policy ARN |

### 2. Creating the CI/CD pipeline in the tools account
- On the AWS CloudFormation console, choose `Create stack`.
- Upload a [template](https://github.com/awslabs/serverless-api-cross-account-cicd/blob/master/cloudformation/source-account/cf-ServerlessDeployPipeline.yml)
- Enter stack name `myapp-cicd-ServerlessDeployPipeline`
- Specify your designated AWS account ID for the target Account in the `TargetAccountID` parameter

This CloudFormation template use the following parameters:
| Parameters | Description | Value |
| --- | --- | --- |
| CFExecutionRoleName | Cross Account Role to be assumed by Cloudformation Service to create serverless resources | cf-execution-role-serverless |
| CodeCommitRepoBranch | The branch name of code commit repo | master |
| CodeCommitRepoName |  The name of code commit repo | my-serverless-api |
| CodePipelineAssumeRoleName | Cross Account Role to be assumed by code pipeline to carry out deployment | cross-account-role-serverless-deployment |
| DeploymentEnvironment | Name of the environment to which the pipeline is deploying | DEV |
| TargetAccountID | Account ID of the target account where the deployment will happen | 123456789012 |


This template returns the following outputs:
| Key | Value | Description | Export Name |
| --- | --- | --- | --- |
| OutCloudWatchPipelineTriggerRoleArn | arn:aws:iam::<ToolsAccountID>:role/Serverless-CloudWatch-Pipeline-Trigger | ARN for CloudWatch Events to trigger CodePipeline | Serverless-CloudWatchPipelineTriggerRoleArn |
| OutCodeBuildRoleArn | arn:aws:iam::<ToolsAccountID>:role/Serverless-CodeBuild-Role | ARN for CodeBuild Role | Serverless-CodeBuildRoleArn |
| OutCodeCommitRepoARN | arn:aws:codecommit:ap-southeast-2:<ToolsAccountID>:my-serverless-api | ARN for the Serverless Lambda Api Repo | my-serverless-lambda-api-repo-arn |
| OutCodeCommitRepoURL | https://git-codecommit.ap-southeast-2.amazonaws.com/v1/repos/my-serverless-api | The URL to be used for Cloning over HTTPS | my-serverless-lambda-api-repo-url |
| OutCodePipeline | Serverless-CodePipeline-my-serverless-api-master | CICD Pipeline Name | Serverless-CodePipelineName |
| OutCodePipelineKMSKeyArn | arn:aws:kms:ap-southeast-2:<ToolsAccountID>:key/<KeyID> | ARN for Pipeline KMS Key | Serverless-CodePipelineKMSKeyArn |
| OutCodePipelineRoleArn | arn:aws:iam::<ToolsAccountID>:role/Serverless-CodePipeline-Role | ARN for CodePipeline Role | Serverless-CodePipelineRoleArn |
| OutCodePipelineS3Bucket | serverless-codepipeline-bucket-ap-southeast-2-<ToolsAccountID> | Name of CodePipeline S3 Bucket | Serverless-CodePipelineS3BucketName |
| OutCodePipelineS3BucketArn | arn:aws:s3:::serverless-codepipeline-bucket-ap-southeast-2-<ToolsAccountID> | ARN of CodePipeline S3 Bucket | Serverless-CodePipelineS3BucketArn |
| OutCodePipelineURL | https://console.aws.amazon.com/codepipeline/home?region=ap-southeast-2#/view/Serverless-CodePipeline-my-serverless-api-master | - | Serverless-CodePipelineUrl |
  
### 3. Deploying the API

#### 3.1  Clone the CodeCommit repository you created earlier
- Generate HTTPS Git credentials for AWS CodeCommit
```bash
$git clone https://<username>:<password>@git-codecommit.ap-southeast-2.amazonaws.com/v1/repos/my-serverless-api
Cloning into 'my-serverless-api'...
warning: You appear to have cloned an empty repository.

```

### 4. Cleanup
