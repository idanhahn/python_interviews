import logging
import logging.config
import os
import sys
import yaml


def logging_setup(default_path, default_level=logging.INFO):
    """
    Setup logging configuration
    """
    if os.path.isfile(default_path):
        with open(default_path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        # todo: needs to be tested
        stderr_handler = logging.StreamHandler(stream=sys.stderr)
        _configure_logger('', default_level, stderr_handler)


color_levels = dict(
    DEBUG='green',
    INFO='cyan',
    WARNING='yellow',
    ERROR='red',
    CRITICAL='red',
)


def _create_formatter():
    BASIC_FORMATTING = "%(asctime)-15s [{}:%(name)s:%(lineno)s:%(funcName)s:%(levelname)s] %(message)s".format(
        os.getpid())
    try:
        from colorlog import ColoredFormatter
        return ColoredFormatter(
            "%(fg_level)s{}%(reset)s".format(BASIC_FORMATTING),
            reset=True, color_levels=color_levels)
    except ImportError:
        # No colorlog? No colors!
        return logging.Formatter(BASIC_FORMATTING)


def _configure_logger(logger_path, min_level, handler, *filters):
    logger = logging.getLogger(logger_path)
    logger.setLevel(min_level)
    handler.setLevel(min_level)
    formatter = _create_formatter()
    handler.setFormatter(formatter)
    for f in filters:
        handler.addFilter(f)
    logger.addHandler(handler)


_cur_log_level = None


def log_to_console(log_level=logging.INFO, file_path=None):
    global _cur_log_level  # this global variable was originally added in order to avoid setting log_level by every test
    if _cur_log_level != log_level:
        _cur_log_level = log_level
        logging.root.setLevel(log_level)
        stderr_handler = logging.StreamHandler(stream=sys.stderr)
        _configure_logger('', log_level, stderr_handler)
        if file_path is not None:
            file_handler = logging.FileHandler(file_path)
            _configure_logger('', log_level, file_handler)
