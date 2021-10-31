import openpyxl
import requests
import game_scrapper as gs
import user_scrapper as us
import excel_filling as ef
import logger_setup
import logging



def main():
    # get steam username from console
    # get steam id from username (Resolve Vanity)
    # get owned games using steam id
    # open a data.xlsx
    # if game in list =>
    #   add username to cell containg the owners
    #   stop
    # else =>
    #   get info from steamspy
    #   get info from steam api
    #   save header img
    #   save all data in data.xlsx
    #   save owner
    #   stop
    logger_setup.init_logging()
    logger = logging.getLogger("logger")
    logger.info("Started the BLITZREVIEW App")
    # workbook = openpyxl.load_workbook('./data.xlsx')
    # x =  gs.get_game_info(823130)
    # print(x)
    # app_ids = us.owned_games_grabber('thedelta28super')
    # for id in app_ids:
    #     logger.debug((gs.get_game_info(id)))

    username = us.username_request()
    appids_list = us.owned_games_grabber(username)
    ef.data_filling(appids_list, username)




if __name__ == '__main__':
    main()