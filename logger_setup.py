import logging
import sys


def init_logging():
    logger = logging.getLogger("logger")
    logger.setLevel(logging.DEBUG)

    fmt = logging.StreamHandler(stream=sys.stdout)
    fmt.setFormatter(logging.Formatter(fmt='[%(filename)s: %(levelname)s] %(message)s'))
    fh = logging.FileHandler("application.log", mode='w')
    logger.addHandler(fmt)
    logger.addHandler(fh)
