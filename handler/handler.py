from sqlalchemy.exc import SQLAlchemyError
from providers import github, stripe, twilio
from common import constants as con
from db.storer import Storer
import logging

logger = logging.getLogger()
EVENT = con.EventHandler

def _persist(envelope):
    """Shared dedup-check + save path, used by every provider."""
    if Storer.webhook_exists(envelope[con.NORM_KEY_DELIVERY_ID]):
        return {**envelope, con.STATUS: EVENT.OK}
    try:
        Storer.save_webhook(envelope)
        return {**envelope, con.STATUS: EVENT.OK}
    except SQLAlchemyError:
        return {con.STATUS: EVENT.ERROR_STORAGE}

def github_event(body_bytes, headers):
    result = github.handle_event(body_bytes, headers)
    if isinstance(result, con.EventHandler):
        return {con.STATUS: result}
    return _persist(result)

def stripe_event(body_bytes, headers):
    result = stripe.handle_event(body_bytes, headers)
    if isinstance(result, con.EventHandler):
        return {con.STATUS: result}
    return _persist(result)

def twilio_event(body_bytes, headers, url=None, form_params=None):
    result = twilio.handle_event(body_bytes, headers, url, form_params)
    if isinstance(result, con.EventHandler):
        return {con.STATUS: result}
    return _persist(result)