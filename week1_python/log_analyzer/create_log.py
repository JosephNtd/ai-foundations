import random
import sys
from datetime import datetime, timezone, timedelta

def make_log(path: str, n_lines: int) -> None:
    with open(path, "w", encoding="utf-8") as f:
        ngay_bat_dau = datetime(2026, 1, 1, tzinfo=timezone(timedelta(hours=7)))
        ngay_ket_thuc = datetime(2026, 12, 31, tzinfo=timezone(timedelta(hours=7)))

        ts_bat_dau = ngay_bat_dau.timestamp()
        ts_ket_thuc = ngay_ket_thuc.timestamp()
        for _ in range(n_lines):
            ip = random.choice(
                [
                    "203.0.113.42",
                    "198.51.100.7",
                    "192.0.2.15"
                ]
            )

            ts_ngau_nhien = random.uniform(ts_bat_dau, ts_ket_thuc)
            dt_ngau_nhien = datetime.fromtimestamp(ts_ngau_nhien, tz=timezone(timedelta(hours=7)))
            time = dt_ngau_nhien.strftime("[%d/%b/%Y:%H:%M:%S %z]")

            url = random.choice(
                [
                    "GET /mod/quiz/attempt.php?attempt=12",
                    "POST /mod/quiz/processattempt.php",
                    "GET /my/view=reading",
                    "POST /my/view=reading",
                    "GET /my/view=listening",
                    "POST /my/view=listening",
                    "GET /my/view=onthi",
                    "POST /my/view=onthi"
                ]
            )

            status_code = random.choice([200, 302, 304, 404, 502])

            f.write(f'{ip} - - {time} "{url} HTTP/1.1" {status_code} 5123 "-" "Mozilla/5.0"\n')

if __name__ == "__main__":
    make_log(sys.argv[1], int(sys.argv[2]))