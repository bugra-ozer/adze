import sqlalchemy
from database import SessionLocal
from models import *

fake_enve={
  "provider": "stripe",
  "event_type": "push",
  "delivery_id": "72d32162e-cc78-11e3-81ab-4c9367dc0958",
  "timestamp": datetime(2026, 8, 10, 14, 32, 1, tzinfo=timezone.utc),
  "raw_payload": {"ref": "refs/heads/main", "pusher": {"name": "octocat"}}
}

session=SessionLocal()

class Storer():

    @staticmethod
    def save_webhook(envelope:dict):
        """Insert into webhook table."""
        provider_local=envelope[con.NORM_KEY_PROVIDER]
        event_type_local=envelope[con.NORM_KEY_EVENT_TYPE]
        delivery_id_local=envelope[con.NORM_KEY_DELIVERY_ID]
        timestamp_local=envelope[con.NORM_KEY_TIMESTAMP]
        raw_payload_local=envelope[con.NORM_KEY_RAW_PAYLOAD]
        provider_id_local=session.query(Provider).filter(Provider.provider_name == provider_local).first().provider_id
        try:
            webhook=Webhook(
                provider_id=provider_id_local,
                event_type=event_type_local,
                delivery_id=delivery_id_local,
                timestamp=timestamp_local,
                raw_payload=raw_payload_local
            )
            session.add(webhook)
            session.commit()
        finally:session.close()

    @staticmethod
    def seed_providers():
        try:
            existing = {p.provider_name for p in session.query(Provider).all()}
            for name in con.PROVIDERS_ALL:
                if name not in existing:
                    session.add(Provider(provider_name=name))
            session.commit()
        finally:session.close()

storer=Storer()
storer.seed_providers()
try: print(storer.save_webhook(fake_enve))
except: print('failed')