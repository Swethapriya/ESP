import logging
import logging.config
import os

SRC_PATH = os.path.normpath(os.getcwd() + 3*(os.sep + os.pardir))

class LogConfig(object):
    """configuring log"""
    def __init__(self,SRC_PATH):
        fname = os.path.join(SRC_PATH , 'src', 'common', 'Logger', 'logging.conf')
        logging.config.fileConfig(fname, disable_existing_loggers = False)
        self.ESP_LOGGER = logging.getLogger('esp_logger')

class ExceptionCatch(LogConfig):
     """configuring log"""
     def Catch(self):
         self.ESP_LOGGER.exception('Exception Occurred')

if __name__ == '__main__':
    LOGGER = LogConfig(SRC_PATH).ESP_LOGGER
    LOGGER.debug("debug works!")
    LOGGER.info("info works!")
    LOGGER.warn("warn works!")
    LOGGER.error("error works!")
    LOGGER.warning("warning works")
    try:
        answer = 2/0
    except Exception as e:
        ExceptionCatch(SRC_PATH).Catch()
