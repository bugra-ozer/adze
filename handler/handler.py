from sqlalchemy.exc import SQLAlchemyError
from providers import github
from common import constants as con
from db.storer import Storer
import logging

logger=logging.getLogger()
EVENT=con.EventHandler

def github_event(body_bytes, headers):
    envelope=github.handle_event(body_bytes, headers)
    if not envelope:
        return {con.STATUS: EVENT.UNAUTHORIZED}
    else:
        if Storer.webhook_exists(envelope[con.NORM_KEY_DELIVERY_ID]): return {con.STATUS: EVENT.OK}
        try:
            Storer.save_webhook(envelope)
            return {con.STATUS: EVENT.OK}
        except SQLAlchemyError: return {con.STATUS: EVENT.ERROR_STORAGE}
