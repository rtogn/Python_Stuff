import inspect
import logging

def customLogger(logLevel):
    #get the name of the class/method from where this is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("{0}.log".format(loggerName), mode = 'a')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(message)s')
                                  
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger

