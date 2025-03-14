import logging
import os

logger = logging.getLogger(__name__)

TRUISH_VALUES = {"true", "yes", "1"}


def parse_bool_flag(env: str) -> bool:
    """Parse the environment variable and evaluate it as a boolean value.

    Default to False.
    """
    return os.environ.get(env, "").lower() in TRUISH_VALUES


def parse_str_list(env: str) -> list[str]:
    """Parse a comma separated string into a string list."""
    raw_value = os.environ.get(env)
    return raw_value.split(",") if raw_value else []
