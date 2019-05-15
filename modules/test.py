import unittest
from encrypt import FernetEncryption as FE
from cryptography.fernet import Fernet


class test_FernetEncryption(unittest.TestCase):
    """
    The test case for the FernetEncryption module
    This case tests to see that the FernetEncryption object 
    can encrypt and decrypt a string using the same Fernet key.
    
    """


    def setUp(self):
        self.key = Fernet.generate_key()

        self.fernet_object = FE(self.key)

        self.msg = b"This is a test message!@#"


    def test_encrypt_message(self):
         self.cipher_txt = self.fernet_object.encrypt_message(self.msg)

         self.msg2 = self.fernet_object.decrypt_message(self.cipher_txt)

         self.assertNotEqual(self.msg, self.cipher_txt)
         self.assertEqual(self.msg, self.msg2)


if __name__ == '__main__':
    unittest.main()
