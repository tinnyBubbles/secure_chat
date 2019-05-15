import unittest
from encrypt import FernetEncryption as FE


"""
-test the FernetEncryption class
    -methods
        -encrypt_message must return c off P
        -decrypt_message must take c and get P
    -FernetEncryption 
        -check that object initializes with fernet key
"""

class test_FernetEncryption(unittest.TestCase):
    def setUp(self):
        self.key = Fernet.generate_key()

        self.fernet_object = FE(key)

        self.msg = b"This is a test message!@#"


    def test_encrypt_message(self):
         self.cipher_txt = self.fernet_object.encrypt_message(self.msg)

         self.msg2 = self.fernet_object.decrypt_message(self.cipher_txt)

         self.assertNotEqual(self.msg, self.cipher_txt)
         self.assertEqual(self.msg, self.msg2)
         

    def tearDown(self):
        self.fernet_object.dispose()
        self.key.dispose()
        self.msg.dispose()


if __name__ == '__main__':
    unittest.main()
