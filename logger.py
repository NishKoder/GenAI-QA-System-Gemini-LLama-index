import logging
import os
from logging.handlers import TimedRotatingFileHandler


LOG_DIR = 'logs'  # Consider making this more customizable


def configure_logging() -> None:
    """
    Creates the logging directory if needed and sets up logger configuration
    """

    os.makedirs(LOG_DIR, exist_ok=True)

    # Time-based log rotation - e.g., a new file every midnight
    handler = TimedRotatingFileHandler(
        os.path.join(LOG_DIR, 'application.log'),
        when='midnight',
        backupCount=10  # Keep 5 backup files
    )

    formatter = logging.Formatter(
        fmt="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    logger = logging.getLogger()  # Get the root logger
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
