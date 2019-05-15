from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac
import os
import sys


backend = default_backend()
salt = bytes(bytearray.fromhex(sys.argv[1]))

kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=backend
        )

mac_salt = bytes(bytearray.fromhex(sys.argv[2]))
mac_kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=mac_salt,
        iterations=100000,
        backend=backend
        )

key = kdf.derive(os.environ['PASSWORD'].encode('utf-8'))
mac_key = mac_kdf.derive(os.environ['PASSWORD'].encode('utf-8'))

nonce     = bytes(bytearray.fromhex(sys.argv[3]))
algorithm = algorithms.ChaCha20(key, nonce)
cipher    = Cipher(algorithm, mode=None, backend=default_backend())
decryptor = cipher.decryptor()
h = hmac.HMAC(mac_key, hashes.SHA256(), backend=default_backend())

for line in sys.stdin:
    print(line[0:64])
    sig = bytes(bytearray.fromhex(line[0:64]))
    print(line.strip()[64:])
    msg = bytes(bytearray.fromhex(line.strip()[64:]))

    h.update(msg)
    h.copy().verify(sig)

    print(decryptor.update(msg))
