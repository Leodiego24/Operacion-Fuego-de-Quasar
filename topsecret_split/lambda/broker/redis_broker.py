import redis
from resources.utils.general_utils import GeneralsUtils
from adapters.cache_adapter import CacheAdapter


class RedisBroker(CacheAdapter):
    """This class is responsible for all interactions with redis
    """

    def __init__(self, parameters):
        """This constructor is in charge of starting the connection with redis
        """

        self.__connection =\
            redis.Redis(
                host=parameters,
                port=6379, db=0)

    def set_data(self, key, value):
        """This method is in charge of send key and
           value to elastic

        Args:
            key_event ([str]): Key to persist in elastic
            data : Data to persist in elastic

        Raises:
            Exception: [description]
        """

        if not GeneralsUtils.validate_string(key) or\
           value is None:
            raise Exception("error value"+ f"{key}")

        self.__connection.set(key, value)

    def get_data(self, key):
        """This method is in charge of search any key in elastic

        Args:
            key ([type]): Key to search

        Raises:
            Exception:  error value

        Returns:
            Key[type]: Data associate to key
        """

        if not GeneralsUtils.validate_string(key):
            raise Exception("error value"+ f"{key}")

        value = self.__connection.get(key)

        return value

    def valid_key(self, key):
        """This method is in valid  any key in elastic

        Args:
            key ([type]): Key to search

        Raises:
            Exception:  error value

        Returns:
            Key[type]: Data associate to key
        """

        if not GeneralsUtils.validate_string(key):
            raise Exception("error value"+ f"{key}")

        value = self.__connection.exists(key)

        return value
