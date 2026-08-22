import sqlalchemy
from db.database import SessionLocal
from db.models import *

class Storer():

    @staticmethod
    def save_webhook(envelope:dict):
        """Insert into webhook table."""
        session = SessionLocal()
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
    def webhook_exists(delivery_id):
        session = SessionLocal()
        try:
            delivery=session.query(Webhook).filter(Webhook.delivery_id == delivery_id).first()
            if delivery: return True
            else: return False
        finally: session.close()

def seed_providers():
    session = SessionLocal()
    try:
        existing = {p.provider_name for p in session.query(Provider).all()}
        for name in con.PROVIDERS_ALL:
            if name not in existing:
                session.add(Provider(provider_name=name))
        session.commit()
    finally:session.close()