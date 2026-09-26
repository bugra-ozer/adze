from flask import Flask, jsonify, request
from handler import handler
from common import constants as con
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)
EVENT = con.EventHandler
app = Flask(__name__)

# Maps internal status -> external HTTP code. External responses stay
# uniform on purpose (no internal-state leakage); logger.info below
# carries the specific status for our own visibility.
STATUS_TO_HTTP = {
    EVENT.OK: 200,
    EVENT.UNAUTHORIZED: 401,
    EVENT.ERROR_PARSE: 400,
    EVENT.ERROR_STORAGE: 500,
}

def _respond(envelope):
    status = envelope[con.STATUS]
    http_code = STATUS_TO_HTTP[status]
    logger.info("webhook result: %s -> %s", status.name, http_code)
    if status == EVENT.OK:
        response_envelope = dict(envelope)
        response_envelope[con.STATUS] = status.value
        return jsonify(response_envelope), 200
    return jsonify(con.ERROR_INVALID_CREDENTIALS), http_code

@app.route('/', methods=['POST'])
def status():
    """Health check."""
    return jsonify('ok'), 200

@app.route('/webhook/github', methods=['POST'])
def webhook_github():
    headers = request.headers
    body_bytes = request.get_data()
    envelope = handler.github_event(body_bytes, headers)
    return _respond(envelope)

@app.route('/webhook/stripe', methods=['POST'])
def webhook_stripe():
    headers = request.headers
    body_bytes = request.get_data()
    envelope = handler.stripe_event(body_bytes, headers)
    return _respond(envelope)

@app.route('/webhook/twilio', methods=['POST'])
def webhook_twilio():
    headers = request.headers
    body_bytes = request.get_data()
    url = request.url
    form_params = request.form.to_dict()
    envelope = handler.twilio_event(body_bytes, headers, url, form_params)
    return _respond(envelope)

if __name__ == '__main__':
    load_dotenv()
    app.run()