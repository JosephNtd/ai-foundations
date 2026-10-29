import tracemalloc
from log_analyzer.models import LogEntry
from collections import Counter
from datetime import datetime
from dataclasses import dataclass
from collections.abc import Iterator, Iterable
PATH = "data/100k_lines.log"

def parse_line(line: str) -> LogEntry:
    quote_part = line.split('"')


    time_str = line.split("[")[1].split("]")[0]
    url = quote_part[1].split("?")[0].split(" ")[1]
    status_code = int(quote_part[2].split(" ")[1])

    time = datetime.strptime(time_str, "%d/%b/%Y:%H:%M:%S %z")
    entry = LogEntry(time=time, url=url, status_code=status_code)

    return entry

def read_entries(path: str) -> Iterator[LogEntry]:
    with open(path, encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            try:
                log = parse_line(line)
                yield log
            except (ValueError, IndexError) as e:
                print(f"Error line {i}: {type(e).__name__}")

@dataclass
class LogStats:
    count_hour: Counter[int]
    top10_url: list[tuple[str, int]]
    count_error: Counter[bool]

    @property
    def error_rate(self) -> float:
        total = self.count_error.total()
        return self.count_error[True] / total * 100 if total else 0

def count_log(entries: Iterable[LogEntry]) -> LogStats:
    count_hour = Counter()
    count_url = Counter()
    count_error = Counter()
    for entry in entries:
        count_hour[entry.time.hour] += 1
        count_url[entry.url] += 1
        count_error[entry.is_server_error()] += 1

    return LogStats(
        count_hour=count_hour,
        top10_url=count_url.most_common(10),
        count_error=count_error
    )

if __name__ == "__main__":
    stats = count_log(read_entries(PATH))

    for time, total in stats.count_hour.items():
        print(f"{time}: {total}")

    for url, total in stats.top10_url:
        print(f"{url}: {total}")

    print(f"{stats.error_rate:.2f}%")