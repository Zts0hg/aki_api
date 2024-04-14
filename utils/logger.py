import logging


def init_logger(file_name):
    """初始化日志器, 输出日志到日志文件和标准输出, 并返回日志器lgsc (logging-shortcut的缩写)
    日志文件同样放在/mnt0/data_quality_files/目录下
    日志文件名为"log_" + file_name去掉扩展名的base_name + ".log"
    """

    logger_name = file_name.split(".")[-2]
    logfile_name = f"log_{logger_name}.log"
    file_handler = logging.handlers.RotatingFileHandler(f"/home/lighthouse/{logfile_name}", mode='a', encoding='utf-8')
    formater = logging.Formatter('[%(asctime)s] %(name)s [%(levelname)s]: %(message)s')
    file_handler.setFormatter(formater)
    logging.getLogger(logger_name).addHandler(logging.StreamHandler(sys.stdout))
    logging.getLogger(logger_name).addHandler(file_handler)
    logging.getLogger(logger_name).setLevel(logging.INFO)
    return logging.getLogger(logger_name)
