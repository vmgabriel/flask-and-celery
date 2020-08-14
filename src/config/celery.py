"""
Module for Celery Configuration
"""

# environments
from src.config.env import configuration as conf


def __get_usr_password() -> str:
    """Build the Base Usr"""
    return f"{conf.get('user_broker')}:{conf.get('pass_broker')}" \
        if conf.get('user_broker') and conf.get('pass_broker') \
        else conf.get('user_broker') if conf.get('user_broker') else ''


def __get_host_port() -> str:
    """Build host port"""
    return f"{conf.get('url_broker')}:{conf.get('port_broker')}" \
        if conf.get('port_broker')  \
        else f"{conf.get('url_broker')}"


def __get_user_host() -> str:
    """Build Url for user"""
    return __get_host_port() \
        if __get_usr_password() == '' \
        else f"{__get_usr_password()}@{__get_host_port()}"


def __get_url_broker() -> str:
    """Build the Url of Block"""
    return f"{conf.get('protocol_broker')}://{__get_user_host()}/"


configuration = {
    'broker': __get_url_broker(),
    'virtual_host': '0',
}
