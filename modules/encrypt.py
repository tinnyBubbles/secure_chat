"""
    E(k, P) --> C
    D(k, C) --> P

    Arguments: 
        k = Fernet key
        P = plain text(bytes) to be encrypted

    Return:
        C = cypher text
"""


from cryptography.fernet import Fernet 


class FernetEncryption(self):
    
    def encrypt_message(self, k, P):
        f = Fernet(k)
        C = f.encrypt(P)

        return C 

    def decrypt_message(self, k, C):
        P = f.decrypt(C)


        return P
