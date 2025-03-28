import logging

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", filename="logfile.log", level=logging.INFO)
logging.info("這條訊息會被寫入 logfile.log")
