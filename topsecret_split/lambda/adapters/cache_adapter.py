import abc


class CacheAdapter(abc.ABC):

    @abc.abstractmethod
    def set_data(self, key, value):
        """ Get parameter"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_data(self, key):
        """ Get parameter"""
        raise NotImplementedError 

    @abc.abstractmethod
    def valid_key(self, key):
        """ Get parameter"""
        raise NotImplementedError