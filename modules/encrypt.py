"""
    This module provides the FernetEncryption class, which 
    contains the definitions encrypt_message and decrypt_message.    
"""


from cryptography.fernet import Fernet 


class FernetEncryption:
    
    def __init__(self, k):
        self.f = Fernet(k)


    def encrypt_message(self, P):
        C = self.f.encrypt(P)


        return C 

    def decrypt_message(self, C):
        P = self.f.decrypt(C)


        return P
