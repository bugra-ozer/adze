#Internal Modules
from db.database import Engine, Base
from db.models import Provider, Webhook, Forward
from db.storer import seed_providers
import app as api

#External Modules
from common import constants as con, constantsdev as condev
from dotenv import load_dotenv
import os

def get_secret(secret_key:str):
    """Try to get key, or raise error."""
    try:
        key=os.getenv(secret_key).encode(condev.UTF_8)
        return key
    except ValueError: raise ValueError(con.ERROR_KEY_NOT_FOUND)

if __name__ == '__main__':
    load_dotenv()
    Base.metadata.create_all(Engine)
    seed_providers()
    api.app.run()