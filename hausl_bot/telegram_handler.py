import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from __init__ import bot_token, valid_users

from hausl_bot.house_status import HouseStatus
from hausl_bot.my_ip_fetcher import MyIPFetcher
from hausl_bot.warn_wetter_fetcher import WarnWetterFetcher
from hausl_bot.weather_data_fetcher import WeatherDataFetcher


class TelegramHandler:
    def __init__(self):
        """Start the bot."""
        # Create the Updater and pass it your bot's token.
        # Make sure to set use_context=True to use the new context based callbacks
        # Post version 12 this will no longer be necessary
        updater = Updater(bot_token, use_context=True)

        # Get the dispatcher to register handlers
        dp = updater.dispatcher

        # on different commands - answer in Telegram
        dp.add_handler(CommandHandler('help', self.__help))
        dp.add_handler(CommandHandler('weatherWarnings', self.__weather_warnings))
        dp.add_handler(CommandHandler('weatherStationValues', self.__weather_station_values))
        dp.add_handler(CommandHandler('whosAtHome', self.__whos_at_home))
        dp.add_handler(CommandHandler('startWashing', self.__start_washing))
        dp.add_handler(CommandHandler('whatsMyBotsIP', self.__whats_my_bots_ip))
        dp.add_handler(CommandHandler('getSystemUptime', self.__get_system_uptime))

        # log all errors
        dp.add_error_handler(self.__error)

        # Start the Bot
        updater.start_polling()

        # Run the bot until you press Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        updater.idle()

    def __help(self, update, context):
        if self.__validate_user(update):
            help_msg = '/help - Shows this help.\r\n'
            help_msg = help_msg + '/weatherWarnings - Shows weather warnings for the configured region.\r\n'
            help_msg = help_msg + '/weatherStationValues - Shows the values from my weatherstation.\r\n'
            help_msg = help_msg + '/whosAtHome - Shows connected devices to the WLAN.\r\n'
            help_msg = help_msg + '/startWashing - Sends you a notification if the washing machine has finished.\r\n'
            help_msg = help_msg + '/whatsMyBotsIP - Sends you the public ip of the host the bot is running on.\r\n '
            help_msg = help_msg + '/getSystemUptime - Sends you the uptime of the system.\r\n '

            update.message.reply_text(help_msg)

    def __weather_warnings(self, update, context):
        if self.__validate_user(update):
            update.message.reply_text(WarnWetterFetcher.get_warnings())

    def __weather_station_values(self, update, context):
        if self.__validate_user(update):
            update.message.reply_text(WeatherDataFetcher.get_current_data())

    def __whos_at_home(self, update, context):
        if self.__validate_user(update):
            update.message.reply_text(HouseStatus.get_house_status())

    def __start_washing(self, update, context):
        if self.__validate_user(update):
            update.message.reply_text('No function added.')

    def __whats_my_bots_ip(self, update, context):
        if self.__validate_user(update):
            update.message.reply_text(MyIPFetcher.fetch_ip())

    def __get_system_uptime(self, update, context):
        if self.__validate_user(update):
            update.message.reply_text(HouseStatus.get_system_uptime())

    def __error(self, update, context):
        """Log Errors caused by Updates."""
        if self.__validate_user(update):
            logging.warning('Update "%s" caused error "%s"', update, context.error)

    def __validate_user(self, update):
        if update.effective_user.username in valid_users:
            return True
        else:
            update.message.reply_text('Your user is not authorized!')
            return False
