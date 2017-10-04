from dpg.base import AbstractGenerator


class GenericGenerator(AbstractGenerator):

    _username = 'none'
    _service = 'none'
    _counter = 0

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

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
