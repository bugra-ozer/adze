from common.verifier import signature_verify
from main import get_secret
from common import constants as con
from datetime import datetime, timezone
import json

def handle_event(body_bytes, headers)-> dict | False:
    """Verify signature, and return normalized packet."""
    msg = body_bytes
    signature_key = con.KEY_GH_SIGNATURE
    prefix = con.PREFIX_GH
    digest_mod = con.DIGEST_MOD_GH
    webhook_secret_key = get_secret(con.WEBHOOK_SECRET_KEY_GH)
    if signature_verify(webhook_secret_key, signature_key, msg, digest_mod, prefix, headers):
        return normalize(body_bytes, headers)
    else:
        return False

def normalize(body_bytes, headers):
    """Standardize keys, attach timestamp, and unpack bytes body."""
    try:
        envelope={
        con.NORM_KEY_PROVIDER: con.PROVIDER_GH,
        con.NORM_KEY_EVENT_TYPE: headers.get(con.KEY_GH_EVENT),
        con.NORM_KEY_DELIVERY_ID: headers.get(con.KEY_GH_DELIVERY),
        con.NORM_KEY_TIMESTAMP: datetime.now(timezone.utc).isoformat(),
        con.NORM_KEY_RAW_PAYLOAD: json.loads(body_bytes)
        }
        return envelope
    except ValueError: return ValueError(con.ERROR_FAILED_PARSE)

