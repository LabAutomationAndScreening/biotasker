import logging
from functools import partial

import pulumi
from pulumi import export
from pulumi_aws.iam import GetPolicyDocumentStatementArgs
from pulumi_aws.iam import GetPolicyDocumentStatementPrincipalArgs
from pulumi_aws.iam import get_policy_document
from pulumi_aws_native import s3

from .pulumi_ephemeral_deploy.utils import append_resource_suffix_template
from .pulumi_ephemeral_deploy.utils import common_tags_native
from .pulumi_ephemeral_deploy.utils import get_aws_account_id
from .pulumi_ephemeral_deploy.utils import get_config_str

logger = logging.getLogger(__name__)


def pulumi_program() -> None:
    """Execute creating the stack."""
    aws_account_id = get_aws_account_id()
    export("aws-account-id", aws_account_id)
    env = get_config_str("proj:env")

    export("env", env)
    append_resource_suffix = partial(append_resource_suffix_template, pulumi.get_project(), pulumi.get_stack(), env)

    # Create Resources Here
    bucket_name = f"{pulumi.get_stack()}.app.biotasker.com"
    website_bucket = s3.Bucket(
        bucket_name,
        bucket_name=bucket_name,
        website_configuration=s3.BucketWebsiteConfigurationArgs(index_document="index.html", error_document="404.html"),
        tags=common_tags_native(),
        public_access_block_configuration=s3.BucketPublicAccessBlockConfigurationArgs(
            block_public_acls=False, block_public_policy=False, ignore_public_acls=False, restrict_public_buckets=False
        ),
    )
    export("website-url", website_bucket.website_url)
    _ = website_bucket.bucket_name.apply(
        lambda bucket_name: s3.BucketPolicy(
            append_resource_suffix("website"),
            bucket=bucket_name,
            policy_document=get_policy_document(
                statements=[
                    GetPolicyDocumentStatementArgs(
                        effect="Allow",
                        principals=[
                            GetPolicyDocumentStatementPrincipalArgs(
                                type="*",
                                identifiers=["*"],  # Allows all principals
                            )
                        ],
                        actions=["s3:GetObject"],
                        resources=[f"arn:aws:s3:::{bucket_name}/*"],
                    ),
                ]
            ).json,
        )
    )
