import aws_cdk as core
import aws_cdk.assertions as assertions

from stack.pulumi_bootstrap import PulumiBootstrap


def test_pulumi_bootstrap_resource_created():
    app = core.App()
    stack = PulumiBootstrap(app, "tmp")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::S3::Bucket", 1)

    template.resource_count_is("AWS::KMS::Key", 1)
    template.has_resource_properties("AWS::KMS::Key", {
        "EnableKeyRotation": assertions.Match.exact(False)
    })
