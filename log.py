import os
import logging

def get_logger(name = None):
    name = name if name else __name__
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    log_file = os.path.join('.', 'log', '') + name + '.log'
    handler = logging.FileHandler(log_file)
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger