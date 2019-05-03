from datetime import datetime
from pytz import timezone

import requests

from __init__ import influxdb_server_name, influxdb_name, ws_station_number

IN_TS_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
OUT_TS_FORMAT = '%d.%m.%Y, %H:%M:%S'


class WeatherDataFetcher:
    @staticmethod
    def get_current_data():
        ret_message = ''
        ts_list = []

        server_url = 'http://' + influxdb_server_name + ':8086/query?db=' + influxdb_name
        station = '"station"=\'' + str(ws_station_number) + '\''
        r_temperature = requests.get(server_url + '&q=SELECT LAST("value") FROM "temperature" WHERE ' + station)
        r_humidity = requests.get(server_url + '&q=SELECT LAST("value") FROM "humidity" WHERE ' + station)
        r_pressure = requests.get(server_url + '&q=SELECT LAST("value") FROM "pressure" WHERE ' + station)

        if r_temperature.status_code == 200:
            ret_message += 'Temperature: ' + str(
                r_temperature.json()['results'][0]['series'][0]['values'][0][1]) + '°C\r\n'
            ts_list.append(
                datetime.strptime(r_temperature.json()['results'][0]['series'][0]['values'][0][0][:-4], IN_TS_FORMAT))
        else:
            ret_message += 'Temperature: Could not fetch\r\n'

        if r_humidity.status_code == 200:
            ret_message += 'Humidity: ' + str(r_humidity.json()['results'][0]['series'][0]['values'][0][1]) + '%\r\n'
            ts_list.append(
                datetime.strptime(r_humidity.json()['results'][0]['series'][0]['values'][0][0][:-4], IN_TS_FORMAT))
        else:
            ret_message += 'Humidity: Could not fetch\r\n'

        if r_pressure.status_code == 200:
            ret_message += 'Pressure: ' + str(r_pressure.json()['results'][0]['series'][0]['values'][0][1]) + ' Hpa\r\n'
            ts_list.append(
                datetime.strptime(r_pressure.json()['results'][0]['series'][0]['values'][0][0][:-4], IN_TS_FORMAT))
        else:
            ret_message += 'Pressure: Could not fetch\r\n'

        # Get timestamp from oldest update
        sorted_ts_list = sorted(ts_list)
        if len(sorted_ts_list) > 0:
            ts_utc = timezone('UTC').localize(sorted_ts_list[0])
            ret_message += 'Last update: ' + ts_utc.astimezone(timezone('Europe/Berlin')).strftime(
                OUT_TS_FORMAT) + '\r\n'

        return ret_message
