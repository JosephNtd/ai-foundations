import sys
import tracemalloc
from log_analyzer.parser import read_entries, count_log

def benchmark(path: str, method: str) -> None:
    tracemalloc.start()

    if method == "list":
        entry_list = list(read_entries(path))
        stats = count_log(entry_list)
    elif method == "generator":
        stats = count_log(read_entries(path))
    else:
        raise ValueError("method phải là list hoặc generator!")

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"File: {path}")
    print(f"Method: {method}")
    print(f"Current: {current / 1_000_000:.2f} MB")
    print(f"Peak: {peak / 1_000_000:.2f} MB")

if __name__ == "__main__":
    benchmark(sys.argv[1], sys.argv[2])
