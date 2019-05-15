"""
    This module provides the FernetEncryption class, which 
    contains the definitions encrypt_message and decrypt_message.

    The FernetEncryption class is used to create objects capable of 
    encrypting and decrypting a plain text or a cipher. 
"""


from cryptography.fernet import Fernet 


class FernetEncryption:
    
    def __init__(self, k):
        self.key = k
        self.f = Fernet(self.key)

    @staticmethod
    def encrypt_message(P):
        return self.f.encrypt(P) 
    

    @staticmethod
    def decrypt_message(C):
        return self.f.decrypt(C)
