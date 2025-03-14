"""Logger Formatters."""

import datetime as dt
from logging import Formatter, LogRecord


class UTCFormatter(Formatter):
    """Log timestamps in UTC."""

    def formatTime(self, record: LogRecord, datefmt: str | None = None) -> str:
        """Similar to original, but using datetime for custom formats."""
        if datefmt:
            ct = dt.datetime.fromtimestamp(record.created, tz=dt.timezone.utc)
            return ct.strftime(datefmt)
        else:
            return super().formatTime(record=record, datefmt=datefmt)
