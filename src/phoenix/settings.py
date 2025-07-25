import logging
from dataclasses import dataclass, field
from typing import Optional

from phoenix.config import LoggingMode


@dataclass
class _Settings:
    """Settings for Phoenix, lazily initialized."""

    # By default, don't log migrations
    log_migrations: bool = field(default=False)
    # By default, Phoenix does not configure its loggers and acts as a library
    logging_mode: LoggingMode = field(default=LoggingMode.DEFAULT)
    # By default, log level is INFO
    logging_level: int = field(default=logging.INFO)
    # By default, log level is WARNING
    db_logging_level: int = field(default=logging.WARNING)
    # By default, migrations are enabled
    disable_migrations: bool = field(default=False)
    # FullStory organization ID for web analytics tracking
    fullstory_org: Optional[str] = field(default=None)


# Singleton instance of the settings
Settings = _Settings()
