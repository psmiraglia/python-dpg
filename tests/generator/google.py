import unittest

from dpg.google import GoogleGenerator


class TestGenericGenerator(unittest.TestCase):

    username = 'alice'
    username_alias_1 = 'alice@gmail.com'
    username_alias_2 = 'ali.ce'
    username_alias_3 = 'Ali.ce'
    service = 'google'
    counter = 0
    passphrase = 's3cr3t'
    bad_passphrase = 'secret'
    password = 'lwM-XhD-J7H-gnw-XEy'

    def test_setter(self):
        g = GoogleGenerator()

        self.assertEqual(g.username, 'none')
        self.assertEqual(g.service, 'none')
        self.assertEqual(g.counter, 0)

        g.service = self.service
        g.counter = self.counter

        self.assertEqual(g.service, self.service)
        self.assertEqual(g.counter, self.counter)

        g.username = self.username
        self.assertEqual(g.username, self.username)
        g.username = self.username_alias_1
        self.assertEqual(g.username, self.username)
        g.username = self.username_alias_2
        self.assertEqual(g.username, self.username)
        g.username = self.username_alias_3
        self.assertEqual(g.username, self.username)

    def test_generate(self):
        g = GoogleGenerator()
        g.service = self.service
        g.counter = self.counter

        g.username = self.username
        self.assertEqual(g.generate(self.passphrase), self.password)
        self.assertNotEqual(g.generate(self.bad_passphrase), self.password)

        g.username = self.username_alias_1
        self.assertEqual(g.generate(self.passphrase), self.password)
        self.assertNotEqual(g.generate(self.bad_passphrase), self.password)

        g.username = self.username_alias_2
        self.assertEqual(g.generate(self.passphrase), self.password)
        self.assertNotEqual(g.generate(self.bad_passphrase), self.password)

        g.username = self.username_alias_3
        self.assertEqual(g.generate(self.passphrase), self.password)
        self.assertNotEqual(g.generate(self.bad_passphrase), self.password)
