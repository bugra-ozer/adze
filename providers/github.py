from app import signature_verify
from main import get_secret
from constant import constants as cons
from datetime import datetime, timezone
import os, json

webhook_secret_key = get_secret(cons.WEBHOOK_SECRET_KEY_GH)
signature_key = cons.KEY_GH_SIGNATURE
prefix = cons.PREFIX_GH
digest_mod = cons.DIGEST_MOD_GH

def handle_event(raw_body, headers):
    """"""
    msg = raw_body
    if signature_verify(webhook_secret_key, signature_key, msg, digest_mod, prefix, headers):
        return normalize(raw_body, headers)
    else:
        return False

def normalize(raw_body, headers):
    """"""
    try:
        envelope={
        cons.NORM_KEY_PROVIDER: cons.PROVIDER_GH,
        cons.NORM_KEY_EVENT_TYPE: headers.get(cons.KEY_GH_EVENT),
        cons.NORM_KEY_DELIVERY_ID: headers.get(cons.KEY_GH_DELIVERY),
        cons.NORM_KEY_TIMESTAMP: datetime.now(timezone.utc),
        cons.NORM_KEY_RAW_PAYLOAD: json.loads(raw_body)
        }
        return envelope
    except ValueError: return ValueError(cons.ERROR_FAILED_PARSE)

