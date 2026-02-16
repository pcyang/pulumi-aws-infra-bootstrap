from aws_cdk import (
    aws_s3 as s3,
    Stack,
    aws_kms as kms
)
from constructs import Construct


class PulumiBootstrap(Stack):
    """
    PulumiBootstrap provision resources needed to run DIY Backend for Pulumi, 
    including a S3 bucket to host the pulumi state, and encryption key to 
    encrypt the state file.

    Args:
        scope (Construct): The scope in which this stack is defined.
        construct_id (str): The unique identifier for this stack.
        **kwargs: Additional keyword arguments passed to the parent Stack class.
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket_name = f"pulumi-state-{self.account}-{self.region}"
        bucket = s3.Bucket(self, "PulumiStateBucket",
                           bucket_name=bucket_name,
                           versioned=True,
                           encryption=s3.BucketEncryption.S3_MANAGED
                           )
        pulumi_state_key_name = f"pulumi-state-key-{self.account}-{self.region}"
        pulumi_state_key = kms.Key(self, pulumi_state_key_name,
                                   # Pulumi currently doesn't support key rotation for the state
                                   # turning this on may break Pulumi state due to unexpected key update.
                                   enable_key_rotation=False,
                                   description="KMS key for Pulumi to encrypt state files in S3",)
