from sqlalchemy.exc import SQLAlchemyError
from providers import github
from common import constants as con
from db.storer import Storer
import logging

logger=logging.getLogger()
EVENT=con.EventHandler

class Handler:

    def github_event(self, body_bytes, headers):
        envelope=github.handle_event(body_bytes, headers)
        if not envelope:
            return {'status': EVENT.UNAUTHORIZED}
        else:
            if Storer.webhook_exists(envelope[con.NORM_KEY_DELIVERY_ID]): return {'status': EVENT.OK}
            try:
                Storer.save_webhook(envelope)
                return {'status': EVENT.OK}
            except SQLAlchemyError: return {'status': EVENT.ERROR_STORAGE}
