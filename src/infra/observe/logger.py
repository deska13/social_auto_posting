import logging
from logging import config as logging_config
from typing import Any


def create_logger() -> None:
    _log_handlers: list[str] = []
    _logging_config: dict[str, Any] = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {},
        "handlers": {},
        "loggers": {"": {"handlers": _log_handlers}},
        "root": {
            "handlers": _log_handlers,
            "level": "DEBUG",
        },
    }
    console_formatter_name = "verbose"
    console_formatter = {
        console_formatter_name: {
            "format": "%(asctime)s - %(name)s.%(funcName)s:%(lineno)d - %(levelname)s - %(message)s"
        }
    }
    console_handlers = {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": console_formatter_name,
        }
    }
    _log_handlers.append("console")
    _logging_config["formatters"].update(console_formatter)
    _logging_config["handlers"].update(console_handlers)
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
    logging_config.dictConfig(_logging_config)
