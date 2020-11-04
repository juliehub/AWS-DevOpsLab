The following capture the steps for practice lab from [AWS DevOps Blogs](https://aws.amazon.com/blogs/devops/multi-branch-codepipeline-strategy-with-event-driven-architecture/)

1. Clone the repository
```bash
[ec2-user@ip-172-31-56-64 ~]$ git clone https://github.com/aws-samples/aws-codepipeline-multi-branch-strategy.git
Cloning into 'aws-codepipeline-multi-branch-strategy'...
remote: Enumerating objects: 37, done.
remote: Counting objects: 100% (37/37), done.
remote: Compressing objects: 100% (34/34), done.
remote: Total 37 (delta 15), reused 11 (delta 3), pack-reused 0
Unpacking objects: 100% (37/37), done.
[ec2-user@ip-172-31-56-64 ~]$ cd aws-codepipeline-multi-branch-strategy
```
2. Create the prerequisite stack
```bash
[ec2-user@ip-172-31-56-64 aws-codepipeline-multi-branch-strategy]$ aws cloudformation deploy --stack-name Setup-Pipeline --template-file Setup.yaml --region ap-southeas
t-2 --capabilities CAPABILITY_NAMED_IAM

Waiting for changeset to be created..
Waiting for stack create/update to complete
Successfully created/updated stack - Setup-Pipeline
```
3. Copy the AWS CloudFormation template to Amazon S3
```bash
[ec2-user@ip-172-31-56-64 aws-codepipeline-multi-branch-strategy]$ aws s3 cp TemplatePipeline.yaml s3://"$(aws sts get-caller-identity --query Account --output text)"-t
emplates/ --acl private
upload: ./TemplatePipeline.yaml to s3://123456789012-templates/TemplatePipeline.yaml
```
4. Copy the seed.zip file to the Amazon S3 bucket
```bash
[ec2-user@ip-172-31-23-24 aws-codepipeline-multi-branch-strategy]$ zip -r seed.zip buildspec
[ec2-user@ip-172-31-23-24 aws-codepipeline-multi-branch-strategy]$ aws s3 cp seed.zip s3://"$(aws sts get-caller-identity --query Account --output text)"-templates/ --a
cl private
upload: ./seed.zip to s3://123456789012-templates/seed.zip  
[ec2-user@ip-172-31-23-24 aws-codepipeline-multi-branch-strategy]$ aws s3 ls s3://"$(aws sts get-caller-identity --query Account --output text)"-templates/
2020-11-03 10:40:42       8324 TemplatePipeline.yaml
2020-11-03 22:00:44        769 seed.zip
```
5. Create the first repository and its pipeline
```bash
[ec2-user@ip-172-31-23-24 aws-codepipeline-multi-branch-strategy]$ RepoName="myapp"
[ec2-user@ip-172-31-23-24 aws-codepipeline-multi-branch-strategy]$ aws cloudformation deploy --stack-name Repo-$RepoName --template-file TemplatePipeline.yaml \
> --parameter-overrides RepositoryName=$RepoName Setup=true \
> --region ap-southeast-2 --capabilities CAPABILITY_NAMED_IAM

Waiting for changeset to be created..
Waiting for stack create/update to complete
Successfully created/updated stack - Repo-myapp
```
6. Create the develop branch
```bash
[ec2-user@ip-172-31-23-24 ~]$ cd aws-codepipeline-multi-branch-strategy/
[ec2-user@ip-172-31-23-24 aws-codepipeline-multi-branch-strategy]$ mkdir myapp
[ec2-user@ip-172-31-23-24 aws-codepipeline-multi-branch-strategy]$ cd myapp
[ec2-user@ip-172-31-23-24 myapp]$ git config --global credential.helper '!aws codecommit credential-helper $@'
[ec2-user@ip-172-31-23-24 myapp]$ git config --global credential.UseHttpPath true
[ec2-user@ip-172-31-23-24 myapp]$ git clone https://git-codecommit.ap-southeast-2.amazonaws.com/v1/repos/myapp
Cloning into 'myapp'...
remote: Counting objects: 5, done.
Unpacking objects: 100% (5/5), done.
[ec2-user@ip-172-31-23-24 myapp]$ git checkout -b develop
Switched to a new branch 'develop'
[ec2-user@ip-172-31-23-24 myapp]$ git push origin develop
Total 0 (delta 0), reused 0 (delta 0)
To https://git-codecommit.ap-southeast-2.amazonaws.com/v1/repos/myapp
 * [new branch]      develop -> develop
```
7. Create the first feature branch
```bash
[ec2-user@ip-172-31-23-24 myapp]$ git checkout -b feature-abc
Switched to a new branch 'feature-abc'
[ec2-user@ip-172-31-23-24 myapp]$ git push origin feature-abc
Total 0 (delta 0), reused 0 (delta 0)
To https://git-codecommit.ap-southeast-2.amazonaws.com/v1/repos/myapp
 * [new branch]      feature-abc -> feature-abc
```
8. Create the first Pull Request
```bash
[ec2-user@ip-172-31-23-24 myapp]$ aws codecommit create-pull-request --title "My Pull Request" \
> --description "Please review these changes by Tuesday" \
> --targets repositoryName=$RepoName,sourceReference=feature-abc,destinationReference=develop \
> --region ap-southeast-2
{
    "pullRequest": {
        "authorArn": "arn:aws:iam::123456789012:user/julie", 
        "description": "Please review these changes by Tuesday", 
        "title": "My Pull Request", 
        "pullRequestTargets": [
            {
                "repositoryName": "myapp", 
                "destinationCommit": "cfdcb52bd45d5f33d8e0f2067d9fe477f93b62c2", 
                "sourceReference": "refs/heads/feature-abc", 
                "sourceCommit": "cfdcb52bd45d5f33d8e0f2067d9fe477f93b62c2", 
                "destinationReference": "refs/heads/develop", 
                "mergeMetadata": {
                    "isMerged": false
                }
            }
        ], 
        "revisionId": "9add19507663cafbb7f3f5c38a77cc9bfcbe7598af69b733e989a67ff00e8b38", 
        "lastActivityDate": 1604466360.357, 
        "pullRequestId": "1", 
        "approvalRules": [], 
        "clientRequestToken": "b44cc263-d719-4fab-a951-e5fe954b9b8a", 
        "pullRequestStatus": "OPEN", 
        "creationDate": 1604466360.357
    }
}
```
9. Execute the Pull Request approval
```bash
[ec2-user@ip-172-31-23-24 myapp]$ aws codecommit merge-pull-request-by-fast-forward --pull-request-id 1 \
> --repository-name $RepoName --region ap-southeast-2
{
    "pullRequest": {
        "authorArn": "arn:aws:iam::123456789012:user/julie", 
        "description": "Please review these changes by Tuesday", 
        "title": "My Pull Request", 
        "pullRequestTargets": [
            {
                "repositoryName": "myapp", 
                "destinationCommit": "cfdcb52bd45d5f33d8e0f2067d9fe477f93b62c2", 
                "sourceReference": "refs/heads/feature-abc", 
                "sourceCommit": "cfdcb52bd45d5f33d8e0f2067d9fe477f93b62c2", 
                "destinationReference": "refs/heads/develop", 
                "mergeMetadata": {
                    "isMerged": true, 
                    "mergeCommitId": "cfdcb52bd45d5f33d8e0f2067d9fe477f93b62c2", 
                    "mergeOption": "FAST_FORWARD_MERGE", 
                    "mergedBy": "arn:aws:iam::123456789012:user/julie"
                }
            }
        ], 
        "revisionId": "9add19507663cafbb7f3f5c38a77cc9bfcbe7598af69b733e989a67ff00e8b38", 
        "lastActivityDate": 1604466504.185, 
        "pullRequestId": "1", 
        "approvalRules": [], 
        "clientRequestToken": "b44cc263-d719-4fab-a951-e5fe954b9b8a", 
        "pullRequestStatus": "CLOSED", 
        "creationDate": 1604466360.357
    }
}
```
10. Cleanup

