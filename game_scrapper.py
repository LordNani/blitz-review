import requests
import logging
import config
import time
import regex as re

REQUEST_COUNTER = 0

def waiting():
    start_time = time.time()
    while True:
        if (int(time.time()) - config.REQUEST_DELAY) > start_time:
            return
        else:
            time.sleep(0.1)

def get_game_info(app_id):
    global REQUEST_COUNTER
    logger = logging.getLogger('logger')

    logger.info('Getting info for app_id: {}'.format(app_id))
    if REQUEST_COUNTER >= config.REQUEST_LIMIT:
        logger.info('Start waiting {} seconds'.format(config.REQUEST_DELAY))
        waiting()
        logger.info('Finished waiting {} seconds'.format(config.REQUEST_DELAY))
        REQUEST_COUNTER = 0

    response_first = requests.get(config.STEAM_INFO_URL.format(app_id))
    main_info = response_first.json()[str(app_id)]

    if not main_info['success']:
        logger.error('Error getting MAIN info for app_id: {}'.format(app_id))
        return None
    else:
        logger.info('Successfully got MAIN info for app_id: {}'.format(app_id))

    main_info = main_info['data']
    main_info = dict((k, main_info[k]) for k in ['name', 'steam_appid', 'developers', 'price_overview', 'release_date', 'is_free']
                                        if k in main_info)
    main_info['app_link'] = config.STEAM_APP_LINK_URL.format(app_id)
    if(main_info['is_free']):
        main_info['price_overview'] = '0$'
    elif main_info.get('price_overview') is not None:
        main_info['price_overview'] = main_info['price_overview']['initial_formatted']
    main_info['release_date'] = main_info['release_date']['date'][-4:]
    if main_info.get('developers') is None:
        main_info['developers'] = 'EMPTY'
    if type(main_info['developers'] is list):
        main_info['developers'] = main_info['developers'][0]
    #getting extra info
    response_second = requests.get(config.STEAMSPY_INFO_URL.format(app_id))
    extra_info = response_second.json()
    if extra_info['name'] is None:
        logger.error('Error getting EXTRA info for app_id: {}'.format(app_id))
    else:
        logger.info('Successfully got EXTRA info for app_id: {}'.format(app_id))

    extra_info = dict((k, extra_info[k]) for k in ['positive', 'negative', 'owners', 'tags']
                                        if k in extra_info)
    if len(extra_info.get('tags')) == 0:
        extra_info.pop('tags')
    else:
        extra_info['tags'] = ', '.join(list(extra_info['tags'].keys())[:3])
        logger.info('Tags of {}: {}'.format(app_id, extra_info['tags']))
    extra_info['total_reviews'] = extra_info['positive'] + extra_info['negative']
    if extra_info.get('total_reviews') != 0:
        extra_info['score'] = int(extra_info['positive'] / extra_info['total_reviews'] * 100)
    result = main_info | extra_info

    REQUEST_COUNTER += 1

    return result


def save_header(app_id, app_name):
    name = re.sub(r'[^A-Za-z0-9\s]+', '', app_name)
    response = requests.get(config.HEADER_URL.format(app_id))

    file = open("{}{}.jpg".format(config.IMG_PATH, name), "wb")
    file.write(response.content)
    file.close()
