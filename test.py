import os
import unittest
from tomber import *
from random import randrange
import Image


class tomberTester(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.pid = str(os.getpid())
        self.tombfile = '.'.join([self.pid, 'tomb'])
        self.keyfile = '.'.join([self.pid, 'key'])
        self.keyfile2 = '.'.join([self.pid, 'key2'])
        self.mountpath = './tmptomb'
        self.passphrase = str(randrange(2 ** 64))
        self.imagefile = '.'.join([self.pid, 'jpg'])
        self.createImage(self.imagefile)

    @classmethod
    def tearDownClass(self):
        os.unlink(self.tombfile)
        os.unlink(self.keyfile)
        os.unlink(self.keyfile2)
        os.unlink(self.imagefile)

    @classmethod
    def createImage(self, imagefile):
        # create a 100x100 white image, to test bury and exhume
        img = Image.new("RGB", (1200, 1200), (255, 255, 255))
        img.save(imagefile)

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

    def test_07_bury(self):
        self.assertTrue(tbury(self.keyfile, self.passphrase, self.imagefile))

    def test_08_exhume(self):
        self.assertTrue(texhume(self.keyfile2, self.passphrase, self.imagefile))

if __name__ == '__main__':
    unittest.main()