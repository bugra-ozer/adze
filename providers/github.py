from common.verify import signature_verify
from main import get_secret
from common import constants as cons
from datetime import datetime, timezone
import json

webhook_secret_key = get_secret(cons.WEBHOOK_SECRET_KEY_GH)
signature_key = cons.KEY_GH_SIGNATURE
prefix = cons.PREFIX_GH
digest_mod = cons.DIGEST_MOD_GH

def handle_event(body_bytes, headers)-> dict | False:
    """Verify signature, and return normalized packet."""
    msg = body_bytes
    if signature_verify(webhook_secret_key, signature_key, msg, digest_mod, prefix, headers):
        return normalize(body_bytes, headers)
    else:
        return False

def normalize(body_bytes, headers):
    """Standardize keys, attach timestamp, and unpack bytes body."""
    try:
        envelope={
        cons.NORM_KEY_PROVIDER: cons.PROVIDER_GH,
        cons.NORM_KEY_EVENT_TYPE: headers.get(cons.KEY_GH_EVENT),
        cons.NORM_KEY_DELIVERY_ID: headers.get(cons.KEY_GH_DELIVERY),
        cons.NORM_KEY_TIMESTAMP: datetime.now(timezone.utc).isoformat(),
        cons.NORM_KEY_RAW_PAYLOAD: json.loads(body_bytes)
        }
        return envelope
    except ValueError: return ValueError(cons.ERROR_FAILED_PARSE)

