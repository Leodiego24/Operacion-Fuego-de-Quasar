import abc


class CacheAdapter(abc.ABC):
    """Interface with cache adapter definition"""
    @abc.abstractmethod
    def set_data(self, key, value):
        """ Set data in cachedb"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_data(self, key):
        """ Get data in cachedb"""
        raise NotImplementedError 

    @abc.abstractmethod
    def valid_key(self, key):
        """ Valid data in cachedb"""
        raise NotImplementedError