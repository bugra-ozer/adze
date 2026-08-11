from flask import Flask, jsonify, request
from providers import github as gh
from common import constants as cons
from dotenv import load_dotenv

load_dotenv()
app=Flask(__name__)

@app.route('/', methods=['POST'])
def status():
    """Health check."""
    return jsonify('ok'), 200

@app.route('/webhook/github', methods=['POST'])
def webhook_github():
    headers=request.headers
    bytes_body=request.get_data()
    envelope=gh.handle_event(bytes_body, headers)
    if envelope:
        return jsonify(envelope), 200
    else:
        return jsonify(cons.ERROR_INVALID_CREDENTIALS), 401

if __name__ == '__main__':
    app.run()