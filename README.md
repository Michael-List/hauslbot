# Hauslbot
Telegram bot for managing my home. I will add more functions in the next weeks.

# Setup
* Install docker + docker-compose
* Clone this repo
* copy .env-example to .env
* Change .env so that it fits your needs
* docker-compose up -d
* Or for raspberry pi (arm): docker-compose -f docker-compose_armv7l.yml up -d

# Description of .env-example
* BOT_TOKEN -> The token of your Telegram bot, for more information: https://core.telegram.org/bots#6-botfather
* WARN_CELL_ID -> Cell id from WarnWetter for your region in Germany. More information: https://blog.mt88.eu/2017/01/19/wetterwarnungen-vom-dwd-verwenden/
* RUNNING_INSIDE_DOCKER -> Set to True if ir runs inside a container
* MONITORED_DEVICES -> The devices the bot should ping at your home for house status
* VALID_USERS -> The Telegram bot will only respond to users which are mentioned here
