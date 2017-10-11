"""
Copyright 2017 Paolo Smiraglia <paolo.smiraglia@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

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
