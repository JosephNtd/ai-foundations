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

# logs = [
#     LogEntry(datetime(2026, 10, 24, 9, 15, 2, 7), "/mod/quiz/attempt.php", 200),
#     LogEntry(datetime(2026, 10, 24, 21, 40, 55, 7), "/mod/quiz/processattempt.php", 502)
# ]

# for log in logs:
#     print(log)