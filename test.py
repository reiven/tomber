import os
import unittest
from tomber import *
from random import randrange


class tomberTester(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.pid = str(os.getpid())
        self.tombfile = '.'.join([self.pid, 'tomb'])
        self.keyfile = '.'.join([self.pid, 'key'])
        self.mountpath = './tmptomb'
        self.passphrase = str(randrange(2 ** 64))

    @classmethod
    def tearDownClass(self):
        os.unlink(self.tombfile)
        os.unlink(self.keyfile)

    def test_01_dig(self):
        self.assertTrue(tdig(self.tombfile, 10))

    def test_02_forge(self):
        self.assertTrue(tforge(self.keyfile, self.passphrase))

    def test_03_lock(self):
        self.assertTrue(tlock(self.tombfile, self.keyfile, self.passphrase))

    def test_04_open(self):
        self.assertTrue(topen(
            self.tombfile, self.keyfile, self.passphrase, self.mountpath
            ))

    def test_05_close(self):
        self.assertTrue(tclose(self.tombfile.split('.')[0]))

    def test_06_resize(self):
        self.assertTrue(tresize(
            self.tombfile, self.keyfile, self.passphrase, 12
            ))

if __name__ == '__main__':
    unittest.main()