import tracemalloc
from collections.abc import Iterator, Iterable
from collections import Counter
from datetime import datetime
from dataclasses import dataclass
from log_analyzer.models import LogEntry

PATH = "data/100k_lines.log"

def parse_line(line: str) -> LogEntry:
    quoted_parts = line.split('"')

    time_str = line.split("[")[1].split("]")[0]
    url = quoted_parts[1].split("?")[0].split(" ")[1]
    status_code = int(quoted_parts[2].split(" ")[1])

    time = datetime.strptime(time_str, "%d/%b/%Y:%H:%M:%S %z")
    entry = LogEntry(time=time, url=url, status_code=status_code)
    return entry

def read_entries(path: str) -> Iterator[LogEntry]:
    with open(path, encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            try:
                log = parse_line(line)
                yield log
            except (IndexError, ValueError) as e:
                print(f"Dòng {i} bị lỗi vì: {type(e).__name__}")

@dataclass
class LogStats:
    count_hour: Counter[int]
    top10_urls: list[tuple[str, int]]
    count_error: Counter[bool]

    @property
    def error_rate(self) -> float:
        total = self.count_error.total()
        return self.count_error[True] / total * 100 if total else 0.0

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
        top10_urls=count_url.most_common(10), 
        count_error=count_error
    )


if __name__ == "__main__":
    # total = 0
    # for total, entry in enumerate(read_entries(PATH), start=1):
    #     print(entry)

    # print(f"Tổng số log: {total}")

    
    # Cách 1
    entry_list = list(read_entries(PATH))
    stats = count_log(entry_list)
    
    count = Counter(entry.time.hour for entry in entry_list)
    for hour, total in sorted(count.items()):
        print(f"{hour}h: {total}")

    count_top10 = Counter(entry.url for entry in entry_list)
    for url, total in count_top10.most_common(10):
        print(url, total)

    count_error = Counter(entry.is_server_error() for entry in entry_list)
    total = count_error.total()
    result = count_error[True] / total * 100 if total else 0
    print(f"Tỷ lệ 5xx {result:.2f}%")

    

    # # Cách 2
    # print("##############################################")
    

    # stats =  count_log(read_entries(PATH))
        

    # for hour, total in sorted(stats.count_hour.items()):
    #     print(f"{hour}h: {total}")

    # for url, total in stats.top10_urls:
    #     print(url, total)

    # print(f"Tỷ lệ 5xx {stats.error_rate:.2f}%")
    
    # sample_lines = [
    #     '203.0.113.42 - - [24/Oct/2026:09:15:02 +0700] "GET /mod/quiz/attempt.php?attempt=123 HTTP/1.1" 200 5123 "-" "Mozilla/5.0"',
    #     '198.51.100.7 - - [24/Oct/2026:03:22:52 +0700] "      " 200 157 "-" "Mozilla/5.0"',
    #     '203.0.113.43 - - [13/Oct/2026:12:10:33 +0700] "GET /mod/quiz/attempt.php?attempt=1 HTTP/1.1" 200 5123 "-" "Mozilla/5.0"'
    #  ]
    # for line in sample_lines:
    #     info_entry = parse_line(line)
    #     print(info_entry)
    #     print(info_entry.time.hour)

