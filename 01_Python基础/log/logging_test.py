import logging

#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG,filename="runlog.log",
    format="%(asctime)s %(filename)s[line:%(lineno)d][%(levelname)s]%(message)s")

logging.debug("debug info")
logging.info("hell python")
logging.warning("warning info")
logging.critical("critical info")