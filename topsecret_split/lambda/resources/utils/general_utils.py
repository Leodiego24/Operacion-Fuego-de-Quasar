import base64
import json
import os
from datetime import datetime


class GeneralsUtils():
    """This class contains generic functions that
       are transversal in the application
    """

    @staticmethod
    def get_variable(key):
        """ Method get the value to key into enviroment variable"""
        if key in os.environ:
            return os.environ[key]
        else:
            print("Not found key into variables.")
            return ""

    @staticmethod
    def validate_string(value):
        """This method validated that a value be string

        Args:
            value ([type]): value to validate

        Returns:
            [boolean]: If the validation is success response True or
                        if the validate is fail response False
        """

        if not isinstance(value, str):
            return False

        if str.strip(value) == "":
            return False

        return True
