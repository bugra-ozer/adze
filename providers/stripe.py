from common.verifier import signature_verify
from common.secrets import get_secret
from common import constants as con
from datetime import datetime, timezone
import json

def handle_event(body_bytes, headers) -> dict | con.EventHandler:
    """Verify signature, and return normalized packet or a specific failure status."""
    raw_signature_header = headers.get(con.KEY_STRIPE_SIGNATURE)
    if not raw_signature_header:
        return con.EventHandler.UNAUTHORIZED

    timestamp, v1_hash = _parse_signature_header(raw_signature_header)
    if timestamp is None or v1_hash is None:
        return con.EventHandler.UNAUTHORIZED

    msg = f"{timestamp}.".encode('utf-8') + body_bytes
    digest_mod = con.DIGEST_MOD_STRIPE
    prefix = con.PREFIX_STRIPE
    webhook_secret_key = get_secret(con.WEBHOOK_SECRET_KEY_STRIPE)

    # signature_verify expects to pull the hash itself via headers.get(signature_key),
    # so we hand it a minimal dict carrying just the already-extracted v1 hash.
    temp_headers = {con.KEY_STRIPE_SIGNATURE: f"{prefix}{v1_hash}"}

    if not signature_verify(webhook_secret_key, con.KEY_STRIPE_SIGNATURE, msg, digest_mod, prefix, temp_headers):
        return con.EventHandler.UNAUTHORIZED
    return normalize(body_bytes, headers)

def _parse_signature_header(raw_signature_header):
    """Split Stripe's 't=...,v1=...' header into its timestamp and v1 hash."""
    timestamp = None
    v1_hash = None
    for part in raw_signature_header.split(','):
        if '=' not in part:
            continue
        key, _, value = part.partition('=')
        if key == 't':
            timestamp = value
        elif key == 'v1':
            v1_hash = value
    return timestamp, v1_hash

def normalize(body_bytes, headers) -> dict | con.EventHandler:
    """Standardize keys, attach timestamp, and unpack bytes body."""
    try:
        parsed_body = json.loads(body_bytes)
        envelope = {
        con.NORM_KEY_PROVIDER: con.PROVIDER_STRIPE,
        con.NORM_KEY_EVENT_TYPE: parsed_body.get('type'),
        con.NORM_KEY_DELIVERY_ID: parsed_body.get('id'),
        con.NORM_KEY_TIMESTAMP: datetime.now(timezone.utc).isoformat(),
        con.NORM_KEY_RAW_PAYLOAD: parsed_body
        }
        return envelope
    except ValueError:
        return con.EventHandler.ERROR_PARSE