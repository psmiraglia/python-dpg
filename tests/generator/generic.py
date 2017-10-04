import unittest

from dpg.generic import GenericGenerator


class TestGenericGenerator(unittest.TestCase):

    username = 'alice'
    service = 'bank'
    counter = 0
    passphrase = 's3cr3t'
    bad_passphrase = 'secret'
    password = 'iwY-VXf-UEG-MoW-K1d'

    def test_setter(self):
        g = GenericGenerator()

        self.assertEqual(g.username, 'none')
        self.assertEqual(g.service, 'none')
        self.assertEqual(g.counter, 0)

        g.username = self.username
        g.service = self.service
        g.counter = self.counter

        self.assertEqual(g.username, self.username)
        self.assertEqual(g.service, self.service)
        self.assertEqual(g.counter, self.counter)

    def test_generate(self):
        g = GenericGenerator()
        g.username = self.username
        g.service = self.service
        g.counter = self.counter
        self.assertEqual(g.generate(self.passphrase), self.password)
        self.assertNotEqual(g.generate(self.bad_passphrase), self.password)
