import math
from resources.utils.general_utils import GeneralsUtils
from constants import Constants


class PostitionUtils():
    """Class with all utils to locations"""

    def get_locations(self, r1,r2,r3):
        """Get location of sender"""
        x1 = Constants.kenoby['position']['x']
        y1 = Constants.kenoby['position']['y']
        x2 = Constants.skywalker['position']['x']
        y2 = Constants.skywalker['position']['y']
        x3 = Constants.sato['position']['x']
        y3 = Constants.sato['position']['y']
        A = 2*x2 - 2*x1
        B = 2*y2 - 2*y1
        C = r1**2 - r2**2 - x1**2 + x2**2 - y1**2 + y2**2
        D = 2*x3 - 2*x2
        E = 2*y3 - 2*y2
        F = r2**2 - r3**2 - x2**2 + x3**2 - y2**2 + y3**2
        x = (C*E - F*B) / (E*A - B*D)
        y = (C*D - A*F) / (B*D - A*E)
        return x,y

    def get_message(self, message1, message2, message3):
        """Get message of sender"""
        message = []
        length = len(message)
        for i in range(len(message1)):
            msg1 = message1[i]
            msg2 = message2[i]
            msg3 = message3[i]

            if(GeneralsUtils.validate_string(msg1) and (not any(message) or message[length - 1] != msg1)):
                message.append(msg1)
            if(GeneralsUtils.validate_string(msg2) and (not any(message) or message[length - 1] != msg2)):
                message.append(msg2)
            if(GeneralsUtils.validate_string(msg3) and (not any(message) or message[length - 1] != msg3)):
                message.append(msg3)
        return " ".join(message)
