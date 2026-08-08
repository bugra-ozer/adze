from flask import Flask, jsonify, request
from constant import constants as cons
import hmac, hashlib

app=Flask(__name__)

@app.route('/', methods=['POST'])
def status():
    return jsonify('ok'), 200

def signature_verify(key:bytes, msg: bytes, digest_mod, signature_key, prefix):
    given_hash=request.headers.get(signature_key)
    if not given_hash: return False
    hash_computed=(hash_compute(key, msg, digest_mod))
    if hash_compare(given_hash.removeprefix(prefix), hash_computed):
        return True
    else: return False

def hash_compute(key, msg, digest_mod):
    return hmac.new(key, msg, digest_mod).hexdigest()

def hash_compare(hash_one, hash_two):
    return hmac.compare_digest(hash_one, hash_two)

if __name__ == '__main__':
    app.run()