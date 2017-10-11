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

import abc
import base64
import hashlib
import re


CHUNK_SEPARATOR = '-'
CHUNK_SIZE = 3
CHUNKS_NUMBER = 5


class AbstractGenerator(abc.ABC):

    @property
    @abc.abstractproperty
    def username(self):
        raise NotImplementedError()

    @username.setter
    @abc.abstractproperty
    def username(self, username):
        raise NotImplementedError()

    @property
    @abc.abstractproperty
    def service(self):
        raise NotImplementedError()

    @service.setter
    @abc.abstractproperty
    def service(self, service):
        raise NotImplementedError()

    @property
    @abc.abstractproperty
    def counter(self):
        raise NotImplementedError()

    @counter.setter
    @abc.abstractproperty
    def counter(self, counter):
        raise NotImplementedError()

    def generate(self, passphrase):
        source = (('%s:%s:%d:%s') %
                  (self.username, passphrase, self.counter, self.service))
        h = hashlib.sha256()
        h.update(bytes(source, 'utf8'))
        e = re.sub(r'[^0-9A-Za-z]', '', base64.b64encode(h.digest()).decode())
        return CHUNK_SEPARATOR.join([
            e[i:i+CHUNK_SIZE] for i in range(
                0,
                CHUNK_SIZE * CHUNKS_NUMBER,
                CHUNK_SIZE
            )
        ])
