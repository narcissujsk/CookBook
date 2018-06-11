from abc import ABCMeta, abstractmethod


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass


class SocketStream(IStream):
    def read(self):
        print('read')

    def write(self):
        super().write()

