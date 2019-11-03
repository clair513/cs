""" Standardized configuration Settings"""

class BaseConfig(object):

    # User Sessions:
    SESSION_PERMANENT = True
    SESSION_TYPE = "filesystem"
    # Main Application configuration:
    SECRET_KEY = "xGYi7Q9xWx513PMztios"
    SECURITY_PASSWORD_SALT = "jantar_mantar_513"
    DEBUG = False


config = {"default": BaseConfig}
