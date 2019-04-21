import requests


class MyIPFetcher:
    @staticmethod
    def fetch_ip():
        r = requests.get('https://api.ipify.org')
        if r.status_code != 200:
            return 'Could not get the ip address. Status: ' + r.status_code

        return 'The public ip is: ' + r.text