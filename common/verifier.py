import hmac

def signature_verify(secret_key:bytes, signature_key, msg: bytes, digest_mod, prefix, headers):
    given_hash=headers.get(signature_key)
    if not given_hash: return False
    hash_computed=(hash_compute(secret_key, msg, digest_mod))
    if hash_compare(given_hash.removeprefix(prefix), hash_computed):
        return True
    else: return False

def hash_compute(secret_key, msg, digest_mod):
    return hmac.new(secret_key, msg, digest_mod).hexdigest()

def hash_compare(hash_one, hash_two):
    return hmac.compare_digest(hash_one, hash_two)