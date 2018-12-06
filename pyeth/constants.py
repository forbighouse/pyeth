import logging
import sys


KAD_ALPHA = 3
BUCKET_SIZE = 16
KAD_ID_SIZE = 256
BUCKET_NUMBER = 17
BUCKET_MIN_DISTANCE = KAD_ID_SIZE - BUCKET_NUMBER
RE_VALIDATE_INTERVAL = 10
REFRESH_INTERVAL = 10

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
LOGGER.addHandler(ch)

K_REQUEST_TIMEOUT = 1.0
K_BOND_EXPIRATION = 86400
K_EXPIRATION = 20
K_MAX_NEIGHBORS = 12
K_PUBKEY_SIZE = 512
K_MAX_KEY_VALUE = 2 ** K_PUBKEY_SIZE - 1

RET_PENDING_OK = 0
RET_PENDING_TIMEOUT = 1