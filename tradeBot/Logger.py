import logging 

class Logger:
    """ Logging 類別，透過 instance 操作 """
    def __init__(self, log_file="logfile.log"):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # 避免重複添加 handler
        if not self.logger.handlers:
            file_handler = logging.FileHandler(log_file, mode="a")
            formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def log(self, message):
        self.logger.info(message)