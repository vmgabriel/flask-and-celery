"""
Module of Environment Configuration
"""

# Libraries
from os import getenv
from dotenv import load_dotenv

load_dotenv()


def __get_url_broker() -> str:
    """Convert to Url Valid"""
    default = 'localhost'
    url_env_name = 'URL_BROKER'
    return getenv(url_env_name) if getenv(url_env_name) else default


configuration = {
    # Broker
    'user_broker': getenv('USER_BROKER'),
    'pass_broker': getenv('PASSWORD_BROKER'),
    'url_broker': __get_url_broker(),
    'port_broker': 6379,
    'protocol_broker': 'redis'
}
