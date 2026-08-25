from flask import Flask, jsonify, request
from handler import handler
from common import constants as con
from dotenv import load_dotenv
import logging

logger=logging.getLogger(__name__)
app=Flask(__name__)

@app.route('/', methods=['POST'])
def status():
    """Health check."""
    return jsonify('ok'), 200

@app.route('/webhook/github', methods=['POST'])
def webhook_github():
    headers=request.headers
    body_bytes=request.get_data()
    envelope=handler.github_event(body_bytes, headers)
    if envelope[con.STATUS]==con.INFO_OK:
        return jsonify(envelope), 200
    else:
        return jsonify(con.ERROR_INVALID_CREDENTIALS), 401

if __name__ == '__main__':
    load_dotenv()
    app.run()