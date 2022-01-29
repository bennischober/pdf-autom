import configparser
import os

config = None

def read_config():
    config = configparser.ConfigParser()
    path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), os.pardir, 'config.ini'))
    config.read(path)
    return config


def get_config():
    # cache config file
    global config
    if config == None:
        # saving config in global space
        config = read_config()
        return config
    else:
        # return cached config data
        return config

def get_libpaths():
    config = get_config()
    return config['LIBPATHS']


def get_readpaths():
    config = get_config()
    return config['READPATHS']


def get_outpaths():
    config = get_config()
    return config['OUTPATHS']
