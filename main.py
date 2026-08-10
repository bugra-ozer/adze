import os, constant.constants as cons

def get_secret(secret_key:str):
    """Try to get key, or raise error."""
    try:
        key=os.getenv(secret_key)
        return key
    except ValueError: raise ValueError(cons.ERROR_KEY_NOT_FOUND)
