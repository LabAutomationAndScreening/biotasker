import logging

from pulumi import export

from .pulumi_ephemeral_deploy.utils import get_aws_account_id
from .pulumi_ephemeral_deploy.utils import get_config

logger = logging.getLogger(__name__)


def pulumi_program() -> None:
    """Execute creating the stack."""
    aws_account_id = get_aws_account_id()
    export("aws-account-id", aws_account_id)
    env = get_config("proj:env")
    export("env", env)

    # Create Resources Here
