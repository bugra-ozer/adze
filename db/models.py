from database import Base
from common import constants as con
from sqlalchemy import Column, Integer, String, LargeBinary, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.postgresql.json import JSONB
from datetime import timezone, datetime

class Provider(Base):
    __tablename__=con.TABLE_NAME_PROVIDERS
    provider_id=Column(Integer, primary_key=True)
    provider_name=Column(String, unique=True, nullable=False)

class Webhook(Base):
    __tablename__=con.TABLE_NAME_WEBHOOKS
    webhook_id=Column(Integer, primary_key=True)
    provider_id=Column(Integer, ForeignKey(f'{con.TABLE_NAME_PROVIDERS}.provider_id'))
    event_type=Column(String(80))
    delivery_id=Column(String(80), unique=True, nullable=False)
    timestamp=Column(DateTime, default=lambda:datetime.now(timezone.utc))
    raw_payload=Column(JSONB)

class Forward(Base):
    __tablename__=con.TABLE_NAME_FORWARDS
    forwards_id=Column(Integer, primary_key=True)
    webhook_id=Column(Integer, ForeignKey(f'{con.TABLE_NAME_WEBHOOKS}.webhook_id'))
    attempt=Column(Integer, default=1)
    status=Column(Enum('pending', 'failed', 'success', name='forward_status'))