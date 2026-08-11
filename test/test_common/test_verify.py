import pytest, unittest.mock as mock, hmac
from common import constants as cons, verify

@pytest.fixture
def config():
    """Setup requirements for test functions."""
    key=cons.TEST_FAKE_KEY
    msg=cons.TEST_FAKE_BODY
    return key, msg

def test_verify_gh(config):
    """"""
    key, msg=config
    digest_mod=cons.DIGEST_MOD_GH
    given_hash=hmac.new(key, msg, digest_mod).hexdigest() # noqa
    computed_hash=verify.hash_compute(key, msg, digest_mod)
    assert hmac.compare_digest(given_hash, computed_hash)