#!/usr/bin/env python3
import os

import aws_cdk as cdk

from stack.pulumi_bootstrap import PulumiBootstrap


app = cdk.App()
PulumiBootstrap(app, "PulumiBootstrap",
                env=cdk.Environment(account=os.getenv(
                    'CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
                )

app.synth()
