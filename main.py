#Modules
from db.database import Engine, Base
from db.models import Provider, Webhook, Forward
from db.storer import seed_providers
import app as api

from common import constants as con, constantsdev as condev
from dotenv import load_dotenv
from datetime import datetime, timezone
import os

fake_enve={
  "provider": "stripe",
  "event_type": "push",
  "delivery_id": "72d32162e-cc78-11e3-81ab-4c9367dc0958",
  "timestamp": datetime(2026, 8, 10, 14, 32, 1, tzinfo=timezone.utc),
  "raw_payload": {"ref": "refs/heads/main", "pusher": {"name": "octocat"}}
}

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