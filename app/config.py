import os


class Config:
    pass


class DevConfig(Config):
    SECRET_KEY = os.getenv('SECRET_KEY', '100% later I will forget to update it ...')
    STEAM_API_KEY = ''
    DEBUG = os.getenv('DEBUG', True)


class ProdConfig(Config):
    DEBUG = os.getenv('DEBUG', False)


conf_dict = dict(
    dev_config=DevConfig,
    prod_config=ProdConfig,
)


# DO NOT FORGET TO UPDATE IT !!!
current_config = conf_dict.get('dev_config')
