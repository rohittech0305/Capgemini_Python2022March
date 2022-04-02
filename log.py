import logging
'''
5 built in levels are:
debug 10
info 20
warning 30
error 40
critical 50
'''
LOG_FORMAT="%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="output.log",level=logging.DEBUG,format=LOG_FORMAT,
                    filemode='w')
logger=logging.getLogger()
logging.debug("This is first messages")
logging.info("This is first messages")
logging.warning("This is first messages")
logging.error("This is first messages")
logging.critical("This is first messages")
