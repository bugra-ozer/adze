import pytest, unittest.mock as mock, hmac # noqa
from common import constants as con, verifier
from common import constantsdev as condev

@pytest.fixture
def config():
    """Setup requirements for test functions."""
    key=condev.FAKE_SIGNATURE
    msg=condev.FAKE_BODY
    return key, msg

def test_verify_hash(config):
    """"""
    key, msg=config
    digest_mod=con.DIGEST_MOD_GH
    computed_hash=hmac.new(key, msg, digest_mod).hexdigest() # noqa
    test_hash=verifier.hash_compute(key, msg, digest_mod)
    assert hmac.compare_digest(computed_hash, test_hash)