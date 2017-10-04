from dpg.base import AbstractGenerator

import re


class GoogleGenerator(AbstractGenerator):

    _username = 'none'
    _service = 'none'
    _counter = 0

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        # lowercase
        u = username.lower()
        # strip '@gmail.com' if present
        u = re.sub(r'@gmail\.com', '', u)
        # remove '.' character (https://support.google.com/a/answer/33386)
        u = re.sub(r'\.', '', u)
        self._username = u

    @property
    def service(self):
        return self._service

    @service.setter
    def service(self, service):
        self._service = service

    @property
    def counter(self):
        return self._counter

    @counter.setter
    def counter(self, counter):
        self._counter = counter
