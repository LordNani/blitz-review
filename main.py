import requests
import gamescrapper
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
    gamescrapper.get_game_info(220)



if __name__ == '__main__':
    main()