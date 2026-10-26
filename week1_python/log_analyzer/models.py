from datetime import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class LogEntry:
    time: datetime
    url: str
    status_code: int

    def is_server_error(self) -> bool:
        """ Check if server is error or not """
        return 500 <= self.status_code <= 599

    