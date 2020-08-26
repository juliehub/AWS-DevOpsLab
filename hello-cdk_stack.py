from aws_cdk import core

from aws_cdk import (
    aws_s3 as s3,
    core
)

class HelloCdkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # define an Amazon S3 bucket in the stack using
        # an L2 construct, the Bucket class
        bucket = s3.Bucket(self, 
        "MyFirstBucket-julie", 
         versioned=True)
