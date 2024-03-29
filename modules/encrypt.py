"""
    This module provides the FernetEncryption class, which 
    contains the definitions encrypt_message and decrypt_message.

    The FernetEncryption class is used to create objects capable of 
    encrypting and decrypting a plain text or a cipher. One instance
    of this class can only decrypt the fernet token (cipher) that
    was generated by that instance. In other words, instance 1 
    can not decrypt what instance 2 encrypted. 

    Official documentation for the cryptography library can be found
    at this address: https://cryptography.io/en/latest/fernet/
"""


from cryptography.fernet import Fernet 


class FernetEncryption:
    
    def __init__(self, k):
        #create a Fernet object
        self.f = Fernet(k)


    def encrypt_message(self, P):
        return self.f.encrypt(P) 
    

    def decrypt_message(self, C):
        return self.f.decrypt(C)
