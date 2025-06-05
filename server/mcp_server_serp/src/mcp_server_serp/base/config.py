import logging
import os
from dataclasses import dataclass


logger = logging.getLogger(__name__)
LOCAL_DEPLOY_MODE = "local"


@dataclass
class SERPConfig:
    """Configuration for SERP MCP Server.

    Required environment variables:
        SERP_ENDPOINT: The access key for authentication
        SERP_TOKEN: The secret key for authentication
    """
    serp_endpoint: str
    serp_token: str


def load_config() -> SERPConfig:

    config = SERPConfig(
        serp_endpoint=os.getenv("SERP_ENDPOINT", ""),
        serp_token=os.getenv("SERP_TOKEN", ""),
    )
    logger.info(f"Success to Loaded configuration")

    return config


SERP_CONFIG = load_config()
