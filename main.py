import requests
from config import HEADER_URL, IMG_PATH

def save_header(app_id, app_name):
    response = requests.get(HEADER_URL.format(app_id))

    file = open("{}{}.jpg".format(IMG_PATH, app_name), "wb")
    file.write(response.content)
    file.close()




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
    save_header(220, "half-life-2")


if __name__ == '__main__':
    main()