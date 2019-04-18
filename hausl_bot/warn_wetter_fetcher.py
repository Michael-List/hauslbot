import json
from datetime import datetime
import requests

from __init__ import warn_cell_id


class WarnWetterFetcher:
    @staticmethod
    def get_warnings():
        warning_msg = 'Derzeit liegen keine Warnungen vor.'
        r = requests.get('http://www.wettergefahren.de/DWD/warnungen/warnapp/warnings.json')

        if r.status_code != 200:
            return 'Warnungen konnten nicht abgerufen werden. Status: ' + r.status_code

        content = r.text.replace('warnWetter.loadWarnings(', '')
        content = content.replace(');', '')

        all_warnings = json.loads(content)['warnings']
        area_warnings = all_warnings.get(warn_cell_id, '')

        if len(area_warnings) > 0:
            warning_msg = ''
            for warning in area_warnings:
                warning_msg = warning['regionName'] + '\r\n'
                warning_msg = warning_msg + 'Beginn: ' + datetime.fromtimestamp(int(warning['start']) / 1000).strftime(
                    '%H:%M:%S %d-%m-%Y') + '\r\n'
                warning_msg = warning_msg + 'Ende: ' + datetime.fromtimestamp(int(warning['end']) / 1000).strftime(
                    '%H:%M:%S %d-%m-%Y') + '\r\n'
                warning_msg = warning_msg + 'Warnung: ' + warning['description'] + '\r\n\r\n'

        return warning_msg
