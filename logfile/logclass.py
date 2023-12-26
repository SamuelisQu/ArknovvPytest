import os
import logging
from logging.handlers import TimedRotatingFileHandler
import datetime
import json

LOG_PATH = "log"
LOG_INFO = '_info.log'
LOG_ERROR = '_error.log'


class logger():
    def __init__(self, prefix_name="flask"):

        if os.path.exists(LOG_PATH):
            pass
        else:
            os.mkdir(LOG_PATH)

        # print(LOG_PATH)
        # 创建日志器，下面创建了两个日志器
        self.info_logger = logging.getLogger("info")
        self.error_logger = logging.getLogger("error")

        self.sh = logging.StreamHandler()  # 创建日志处理器，在控制台打印

        # 创建一个格式器对象
        self.format = logging.Formatter('[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s]\
    [%(filename)s:%(lineno)d]' '[%(levelname)s] : %(message)s')

        # info_logger日志的设置
        # 创建一个FileHandler处理器对象，并对输出消息的格式进行设置，将其添加到logger，然后将日志写入到指定的文件中
        info_file_handler = logging.FileHandler("%s/%s%s" % (LOG_PATH, prefix_name, LOG_INFO), encoding="utf-8")
        # 为处理器添加格式
        info_file_handler.setFormatter(self.format)

        # error_logger日志的设置
        # 创建一个FileHandler处理器对象，并对输出消息的格式进行设置，将其添加到logger，然后将日志写入到指定的文件中
        error_file_handler = logging.FileHandler("%s/%s%s" % (LOG_PATH, prefix_name, LOG_ERROR), encoding="utf-8")
        # 为处理器添加格式
        error_file_handler.setFormatter(self.format)

        # 为日志处理器info_file_handler添加处理方式，将设置格式后的处理器对象给日志器“吞吃”，
        # 使日志器info_logger有处理日志的能力
        self.info_logger.addHandler(info_file_handler)
        self.error_logger.addHandler(error_file_handler)
        # 指定日志器info_logger的最低输出级别
        self.info_logger.setLevel(logging.DEBUG)
        self.error_logger.setLevel(logging.ERROR)

    def debug(self, msg, *args, **kwargs):
        self.info_logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        # print('进入info级别')
        self.info_logger.info(msg, *args, **kwargs)

    def warn(self, msg, *args, **kwargs):
        self.info_logger.warning(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.info_logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.error_logger.error(msg, *args, **kwargs)

    def fatal(self, msg, *args, **kwargs):
        self.error_logger.fatal(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        self.error_logger.critical(msg, *args, **kwargs)


if __name__ == '__main__':
    logerdata = logger()
    logerdata.debug('debug9')
    logerdata.info('info9')
    logerdata.warn('warn9')
