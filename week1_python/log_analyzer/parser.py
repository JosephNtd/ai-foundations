from datetime import datetime
from log_analyzer.models import LogEntry

def parse_line(line: str) -> LogEntry:
    quoted_parts = line.split('"')

    time_str = line.split("[")[1].split("]")[0]
    url = quoted_parts[1].split("?")[0].split(" ")[1]
    status_code = int(quoted_parts[2].split(" ")[1])

    time = datetime.strptime(time_str, "%d/%b/%Y:%H:%M:%S %z")
    entry = LogEntry(time=time, url = url, status_code= status_code)
    return entry

if __name__ == "__main__":
    sample_lines = [
        '203.0.113.42 - - [24/Oct/2026:09:15:02 +0700] "GET /mod/quiz/attempt.php?attempt=123 HTTP/1.1" 200 5123 "-" "Mozilla/5.0"',
        '198.51.100.7 - - [24/Oct/2026:03:22:52 +0700] "POST /mod/quiz/processattempt.php HTTP/1.1" 200 157 "-" "Mozilla/5.0"',
        '203.0.113.43 - - [13/Oct/2026:12:10:33 +0700] "GET /mod/quiz/attempt.php?attempt=1 HTTP/1.1" 200 5123 "-" "Mozilla/5.0"'
     ]
    for line in sample_lines:
        info_entry = parse_line(line)
        print(info_entry)
        print(info_entry.time.hour)
        
