# pulumi-aws-infra-bootstrap
CDK package for bootstrapping resources needed to run pulumi, such as the S3 bucket for the state and the KMS key for the encryption.

## Getting Started
For the first time on a new account using this CDK, run CDK Bootstrap first.
```
cdk bootstrap
```

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation