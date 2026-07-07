import sys
import time

if __name__ == "__main__":
    N = 1_000_000_000
    if len(sys.argv) > 1:
        N = int(sys.argv[1])

    total = 0

    start = time.perf_counter()

    for i in range(N):
        total += i

    end = time.perf_counter()

    print(f"Sum: {total}")
    print(f"Time: {end - start:.6f} s")