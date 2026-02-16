from aws_cdk import (
    aws_s3 as s3,
    Stack,
    aws_kms as kms
)
import aws_cdk as cdk
from constructs import Construct


class PulumiBootstrap(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket_name = f"pulumi-state-{cdk.Aws.ACCOUNT_ID}-{cdk.Aws.REGION}"
        bucket = s3.Bucket(self, "PulumiStateBucket",
                           bucket_name=bucket_name,  # specify a unique bucket name
                           versioned=True,  # enable versioning for the bucket
                           encryption=s3.BucketEncryption.S3_MANAGED  # use S3-managed encryption
                           )
        pulumi_state_key_name = f"pulumi-state-key-{self.account}-{self.region}"
        pulumi_state_key = kms.Key(self, pulumi_state_key_name,
                                   enable_key_rotation=False,
                                   description="KMS key for Pulumi to encrypt state files in S3",)
