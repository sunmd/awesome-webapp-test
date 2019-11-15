#!/usr/bin/env python3
# -*-encoding:utf-8-*-
import logging

logger = logging.getLogger(__name__)

handleStr = logging.StreamHandler()
handleFile = logging.FileHandler(filename=r"../log/logFile.log")

logger.setLevel(logging.DEBUG)
handleStr.setLevel(logging.DEBUG)
handleFile.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")

handleStr.setFormatter(formatter)
handleFile.setFormatter(formatter)

logger.addHandler(handleStr)
logger.addHandler(handleFile)

def infoLog(*arges, **kw):
	logger.info(*arges, **kw)

def debugLog(*arges, **kw):
	logger.debug(*arges, **kw)
	
def warningLog(*arges, **kw):
	logger.warning(*arges, **kw)

def errorLog(*arges, **kw):
	logger.error(*arges, **kw)

if __name__ == '__main__':

	infoLog("logger mudel is import ok !")
	debugLog("logger mudel is import ok !")
	warningLog("logger mudel is import ok !")
	errorLog("logger mudel is import ok !")
