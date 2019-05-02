import os
from dotenv import load_dotenv
from pathlib import Path

# Load local .env from root folder of the project if not in docker container
if not os.getenv('RUNNING_INSIDE_DOCKER', False):
    load_dotenv(verbose=True)
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)

bot_token = os.environ['BOT_TOKEN']
warn_cell_id = os.environ['WARN_CELL_ID']
monitored_devices = os.environ['MONITORED_DEVICES'].split(',')
valid_users = os.environ['VALID_USERS'].split(',')

# Weatherstuff
influxdb_server_name = os.environ['INFLUXDB_SERVER_NAME']
influxdb_name = os.environ['INFLUXDB_NAME']
ws_station_number = os.environ['WS_STATION_NUMBER']
