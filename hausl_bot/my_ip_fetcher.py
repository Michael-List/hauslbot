import requests


class MyIPFetcher:
    @staticmethod
    def fetch_ip():
        r = requests.get('https://api.ipify.org')
        if r.status_code != 200:
            return 'Die IP-Adresse konnte nicht abgerufen werden. Status: ' + r.status_code

        return 'Die derzeitige öffentliche IP-Adresse ist ' + r.text