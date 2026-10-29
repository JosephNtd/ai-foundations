from datetime import datetime, timedelta, timezone
import pytest
from collections import Counter
from log_analyzer.parser import parse_line, count_log
from log_analyzer.models import LogEntry

def test_error_line():
    with pytest.raises(IndexError):
        parse_line("kjgiutgiyu")

@pytest.mark.parametrize(
    "line, expected_url, expected_hour, expected_status_code",
    [('203.0.113.42 - - [24/Oct/2026:09:15:02 +0700] "GET /mod/quiz/attempt.php?attempt=123 HTTP/1.1" 200 5123 "-" "Mozilla/5.0"',
        "/mod/quiz/attempt.php",
        9,
        200),
        ('198.51.100.7 - - [24/Oct/2026:03:22:52 +0700] "POST /mod/quiz/processattempt.php HTTP/1.1" 200 157 "-" "Mozilla/5.0"',
        "/mod/quiz/processattempt.php",
        3,
        200),
        ('203.0.113.43 - - [13/Oct/2026:12:10:33 +0700] "GET /mod/quiz/attempt.php?attempt=1 HTTP/1.1" 200 5123 "-" "Mozilla/5.0"',
        "/mod/quiz/attempt.php",
        12,
        200),
        ('212.0.113.42 - - [25/Oct/2026:09:15:02 +0700] "GET /mod/quiz/attempt.php?attempt=123 HTTP/1.1" 200 5123 "-" "Mozilla/5.0"',
        "/mod/quiz/attempt.php",
        9,
        200),
        ('123.51.100.7 - - [26/Oct/2026:03:22:52 +0700] "POST /mod/quiz/processattempt.php HTTP/1.1" 502 157 "-" "Mozilla/5.0"',
        "/mod/quiz/processattempt.php",
        3,
        502)
        ]
    )
def test_parse_line(line, expected_url, expected_hour, expected_status_code):
    entry = parse_line(line)

    assert entry.url == expected_url
    assert entry.time.hour == expected_hour
    assert entry.status_code == expected_status_code

def test_count_log():
    logs = [
        LogEntry(datetime(2026, 10, 24, 9, 15, 2, tzinfo=timezone(timedelta(hours=7))), "/mod/quiz/attempt.php", 200),
        LogEntry(datetime(2026, 10, 24, 21, 40, 55, tzinfo=timezone(timedelta(hours=7))), "/mod/quiz/processattempt.php", 502),
        LogEntry(datetime(2026, 10, 24, 9, 40, 55, tzinfo=timezone(timedelta(hours=7))), "/mod/quiz/processattempt.php", 502),
        LogEntry(datetime(2026, 10, 24, 9, 15, 2, tzinfo=timezone(timedelta(hours=7))), "/mod/quiz/processattempt.php", 200),
        LogEntry(datetime(2026, 10, 24, 9, 40, 55, tzinfo=timezone(timedelta(hours=7))), "/mod/quiz/attempt.php", 502),
                
    ]

    stats = count_log(logs)

    assert stats.count_hour == Counter({9: 4, 21: 1})
    assert stats.count_error == Counter({True: 3, False: 2})
    assert stats.top10_urls == [("/mod/quiz/processattempt.php", 3),("/mod/quiz/attempt.php", 2)]
    assert stats.error_rate == 60.00

def test_count_log_0():
    stats = count_log([])
    assert stats.error_rate == 0