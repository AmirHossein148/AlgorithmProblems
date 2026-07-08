import subprocess
import sys
import random
import time

# ---------- CONFIG ----------
fast_file = "Chocolate justice.py"
brute_file = "Chocolate justice 2.py"

# ---------- GENERATE RANDOM TEST CASE ----------
def generate_test_case():
    n = random.randint(1000,2000)        # smaller n for fast testing
    m = random.randint(1000, min(2000, n+10))
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    c = random.randint(1, 100)

    choc_blocks = []
    for _ in range(n):
        x1 = random.randint(0, a-1)
        x2 = random.randint(x1+1, a)
        y1 = random.randint(0, b-1)
        y2 = random.randint(y1+1, b)
        z1 = random.randint(0, c-1)
        z2 = random.randint(z1+1, c)
        choc_blocks.append((x1, y1, z1, x2, y2, z2))

    lines = [f"{n} {m}", f"{a} {b} {c}"]
    for block in choc_blocks:
        lines.append(" ".join(map(str, block)))
    return "\n".join(lines) + "\n"

# ---------- RUN PYTHON FILE WITH TIME ----------
def run_solution(file, input_data):
    start = time.perf_counter()
    result = subprocess.run(
        [sys.executable, file],
        input=input_data.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    end = time.perf_counter()
    exec_time = end - start

    if result.returncode != 0:
        print(f"Error running {file}:\n", result.stderr.decode())
        return None, exec_time
    return result.stdout.decode().splitlines(), exec_time

# ---------- TEST LOOP ----------
eps = 1e-4
num_tests = 5

for t in range(1, num_tests+1):
    print(f"=== Random Test {t} ===")
    input_data = generate_test_case()

    fast_output, fast_time = run_solution(fast_file, input_data)
    brute_output, brute_time = run_solution(brute_file, input_data)

    if fast_output is None or brute_output is None:
        print("Error running solutions.")
        continue

    # ---------- COMPARE OUTPUTS ----------
    ok = True
    for i, (f, b) in enumerate(zip(fast_output, brute_output)):
        try:
            f_val = float(f)
            b_val = float(b)
        except:
            f_val = f
            b_val = b

        if isinstance(f_val, float) and isinstance(b_val, float):
            if abs(f_val - b_val) > eps:
                print(f"Mismatch at cut {i}: fast={f_val}, brute={b_val}")
                ok = False
        else:
            if f_val != b_val:
                print(f"Mismatch at line {i}: fast='{f_val}', brute='{b_val}'")
                ok = False

    if ok:
        print("OK ✔ Outputs match")

    # ---------- PRINT EXECUTION TIME ----------
    print(f"Fast solution time: {fast_time:.6f} s")
    print(f"Brute solution time: {brute_time:.6f} s\n")