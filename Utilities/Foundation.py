import logging
import inspect
import pytest




@pytest.mark.usefixtures("")

class Foundation:

        def getlogger(self):
            loggerName = inspect.stack()
            logger = logging.getlogger(nameOfLogger)
            fileHandler = logging.FileHandler('fileForLogging.log')
            formatter = logging.formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
            fileHandler.setFormatter(formatter)
            logger.addHandler(fileHandler)
            logger.setLevel(logging.DEBUG)
            return logger
