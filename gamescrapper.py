import requests
import logging
import config
import secret
import config as cfg

def get_game_info(app_id):
    logger = logging.getLogger('logger')

    first_res = requests.get(config.STEAM_INFO_URL.format(app_id))
    logger.info('Getting info for app_id: {}'.format(app_id))


def save_header(app_id, app_name):
    response = requests.get(config.HEADER_URL.format(app_id))

    file = open("{}{}.jpg".format(config.IMG_PATH, app_name), "wb")
    file.write(response.content)
    file.close()
