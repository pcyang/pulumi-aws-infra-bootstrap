# pulumi-aws-infra-bootstrap
CDK package for bootstrapping resources needed to run pulumi, such as the S3 bucket for the state and the KMS key for the encryption.

## Getting Started
Setup your AWS Credential using
```
aws login
```

For the first time on a new account using this CDK, run CDK Bootstrap first.
```
cdk bootstrap
```

After that you should be able to deploy the bootstrap by calling
```
cdk deploy
```

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

## Dependencies

This project uses the following third-party libraries:

- [aws-cdk-lib](https://github.com/aws/aws-cdk) - Licensed under the Apache-2.0 License.
- [constructs](https://github.com/aws/constructs) - Licensed under the Apache-2.0 License.
- [typing-extensions](https://github.com/python/typing_extensions) - Licensed under the PSF License.
- [ruff](https://github.com/charliermarsh/ruff) - Licensed under the MIT License.

The Apache-2.0 license file is included in the `third_party/` directory.