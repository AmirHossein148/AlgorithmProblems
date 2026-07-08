import subprocess
import time
import random

CODE_1 = 'code n^2.py'  # Brute Force
CODE_2 = 'code n*log n.py'  # Optimized Sweep-line
NUM_TESTS = 5


def generate_large_test(n_size):
    """Generates a larger test case to really test the speed difference."""
    m = 10 ** 6
    input_str = f"{n_size} {m}\n"
    for _ in range(n_size):
        pos = random.randint(0, m)
        direction = random.choice(['U', 'D'])
        input_str += f"{pos} {direction}\n"
    return input_str


def run_with_timer(filename, input_data):
    start = time.perf_counter()
    process = subprocess.Popen(
        ['python', filename],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input=input_data)
    end = time.perf_counter()

    return stdout.strip(), (end - start)


# Main comparison loop
# We increase N each time to see the "O(N^2) wall"
for n_val in [10**4, 10**5, 10**6]:
    test_input = generate_large_test(n_val)

    out1, time1 = run_with_timer(CODE_1, test_input)
    out2, time2 = run_with_timer(CODE_2, test_input)

    status = "✅ MATCH" if out1 == out2 else "❌ MISMATCH"

    print(f"--- N = {n_val} ---")
    print(f"Status: {status}")
    print(f"Code 1 (Brute): {time1:.4f} seconds")
    print(f"Code 2 (Sweep): {time2:.4f} seconds")
    if time2 > 0:
        print(f"Speedup: {time1 / time2:.1f}x faster")
    print()