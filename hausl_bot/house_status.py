import os

from __init__ import monitored_devices


class HouseStatus:
    @staticmethod
    def get_house_status():
        ret_msg = ''

        for device in monitored_devices:
            ip_address, name = device.split('=')

            # Get online devices
            response = os.system("ping -4 -c 1 -w4 " + ip_address + " > /dev/null 2>&1")
            if response == 0:
                ret_msg = ret_msg + name + ' ist erreichbar.\r\n'
            else:
                ret_msg = ret_msg + name + ' ist NICHT erreichbar.\r\n'

        return ret_msg
