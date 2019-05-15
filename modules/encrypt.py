from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac
import os
import sys


backend = default_backend


salt = os.urandom(16)
kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                 length=32,
                 salt=salt,
                 iterations=100000
                 backend=backend
                )


mac_salt = os.urandom(16)
mac_kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                     length=32
                     salt=salt,
                     iterations=100000
                     backend=backend
                    )

nonce = os.urandom(16)


algorithm = algorithms.ChaCha20(key, nonce)
cipher = Cipher(algorithm, mode=None, backend=default_backend())
encryptor = cipher.encryptor()
h = hmac.HMAC(mac_key, hashes.SHA256(), backend=default_backend())


for line in sys.stdin:
    ct = encryptor.update(line.encode('utf-8'))
    h.update(ct)
    msg = h.copy().finalize() + ct
    print(bytearray(msg).hex())
