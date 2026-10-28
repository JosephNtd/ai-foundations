from collections.abc import Iterator
from collections import Counter
from datetime import datetime
from log_analyzer.models import LogEntry

PATH = "data/sample.log"

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


if __name__ == "__main__":
    # total = 0
    # for total, entry in enumerate(read_entries(PATH), start=1):
    #     print(entry)

    # print(f"Tổng số log: {total}")

    count = Counter(entry.time for entry in read_entries(PATH))
    for url, total in count.items():
        print(url, total)

    count_top10 = Counter(entry.url for entry in read_entries(PATH))
    for url, total in count_top10.most_common(10):
        print(url, total)

    count_status_code = Counter(entry.status_code for entry in read_entries(PATH))
    total = count_status_code.total()
    rate_502 = count_status_code.get(502, 0) / total * 100 if total else 0
    print(f"Tỷ lệ HTTP 502: {rate_502:.2f}%")
    # sample_lines = [
    #     '203.0.113.42 - - [24/Oct/2026:09:15:02 +0700] "GET /mod/quiz/attempt.php?attempt=123 HTTP/1.1" 200 5123 "-" "Mozilla/5.0"',
    #     '198.51.100.7 - - [24/Oct/2026:03:22:52 +0700] "POST /mod/quiz/processattempt.php HTTP/1.1" 200 157 "-" "Mozilla/5.0"',
    #     '203.0.113.43 - - [13/Oct/2026:12:10:33 +0700] "GET /mod/quiz/attempt.php?attempt=1 HTTP/1.1" 200 5123 "-" "Mozilla/5.0"'
    #  ]
    # for line in sample_lines:
    #     info_entry = parse_line(line)
    #     print(info_entry)
    #     print(info_entry.time.hour)

