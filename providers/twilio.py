from common.verifier import hash_compare
from common.secrets import get_secret
from common import constants as con
from datetime import datetime, timezone
import hmac, hashlib, base64

def handle_event(body_bytes, headers, url, form_params) -> dict | con.EventHandler:
    """Verify signature (URL+params scheme, not body), and return normalized packet or a specific failure status."""
    given_signature = headers.get(con.KEY_TWILIO_SIGNATURE)
    if not given_signature:
        return con.EventHandler.UNAUTHORIZED

    webhook_secret_key = get_secret(con.WEBHOOK_SECRET_KEY_TWILIO)
    msg = _build_signed_string(url, form_params)

    computed_hash = hmac.new(webhook_secret_key, msg.encode('utf-8'), hashlib.sha1).digest()
    computed_signature = base64.b64encode(computed_hash).decode('utf-8')

    if not hash_compare(given_signature, computed_signature):
        return con.EventHandler.UNAUTHORIZED
    return normalize(form_params)

def _build_signed_string(url, form_params):
    """Twilio signs: URL + each sorted param key/value concatenated directly (no separators)."""
    signed_string = url
    for key in sorted(form_params.keys()):
        signed_string += key + form_params[key]
    return signed_string

def normalize(form_params) -> dict | con.EventHandler:
    """Standardize keys from Twilio's form-encoded params (no JSON body to parse)."""
    if not form_params:
        return con.EventHandler.ERROR_PARSE
    envelope = {
        con.NORM_KEY_PROVIDER: con.PROVIDER_TWILIO,
        con.NORM_KEY_EVENT_TYPE: form_params.get('EventType') or form_params.get('SmsStatus'),
        con.NORM_KEY_DELIVERY_ID: form_params.get('MessageSid'),
        con.NORM_KEY_TIMESTAMP: datetime.now(timezone.utc).isoformat(),
        con.NORM_KEY_RAW_PAYLOAD: form_params
    }
    return envelope