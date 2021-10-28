import requests
import config
import logger_setup
import logging
from secret import API_KEY

def steamid_converter(username):
    response = requests.get(config.STEAM_ID_URL.format(API_KEY, username))
    username = response.json()['response']['steamid']
    return username

def owned_games_grabber(username):
    logger_setup.init_logging()
    logger = logging.getLogger('logger')
    logger.info('Grabbing games: username {}'.format(username))
    response = requests.get(config.OWNED_GAMES_URL.format(API_KEY, username))
    if response.status_code != 200:
        steamid = steamid_converter(username)
        response = requests.get(config.OWNED_GAMES_URL.format(API_KEY, steamid))
    owned_games_json = response.json()['response']['games']
    appids_list = [game['appid'] for game in owned_games_json]
    logger.info('Success: appids of the {}: {}'.format(username, appids_list))
    return appids_list
