import os

from __init__ import monitored_devices
from uptime import uptime


class HouseStatus:
    @staticmethod
    def get_house_status():
        ret_msg = ''

        for device in monitored_devices:
            ip_address, name = device.split('=')

            # Get online devices
            response = os.system('ping -4 -c 1 -w4 ' + ip_address + ' > /dev/null 2>&1')
            if response == 0:
                ret_msg = ret_msg + name + ' is conected.\r\n'
            else:
                ret_msg = ret_msg + name + ' is not connected.\r\n'

        return ret_msg

    @staticmethod
    def get_system_uptime():
        return uptime
