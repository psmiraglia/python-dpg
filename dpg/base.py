import abc
import base64
import getpass
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

    def generate(self):
        pp_1 = getpass.getpass("[?] Passphrase: ")
        pp_2 = getpass.getpass("[?] Passphrase (again): ")

        if pp_1 != pp_2:
            print("[!] Passphrases are not equal!!!")
            return ''

        source = (('%s:%s:%d:%s') %
                  (self.username, pp_1, self.counter, self.service))
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
