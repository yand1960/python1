import logging

# Конфиуграция логгера
logger = logging.getLogger("mylogger")
logger.addHandler(logging.StreamHandler())
handler = logging.FileHandler("data/log.txt")
handler.setFormatter(logging.Formatter(fmt="%(asctime)s %(levelname)s\t %(message)s"))
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Демнострация использования
if __name__ == "__main__":
    logger.debug("It is debug")
    logger.info("It is info")
    logger.warning("It is warning")
    logger.error("It is error")
    logger.critical("It is critical")