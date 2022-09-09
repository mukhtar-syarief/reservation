import os



def get_config(name, default=None):
    return os.environ.get(name, default)