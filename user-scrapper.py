import os
import requests
import openpyxl
import logging
import config
from secret import API_KEY

def steamid_converter(username):
    response = requests.get(config.STEAM_ID_URL.format(API_KEY, username))
    print(response.json()['response'])


def games_grabber():
    logger = logging.getLogger('logger')
    username = steamid_converter(input('Enter Steam username: '))


    logger.debug('log: ')
    return username


if __name__ == '__main__':
    games_grabber()
    # 'lokan141'