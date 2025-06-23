import sys
import random
import subprocess
from pathlib import Path
import math

# --- Configuration ---
SOLUTION_CPP_NAME = "SerinityFrostfire.cpp"

# --- Path Setup ---
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
SOLUTIONS_DIR = PROJECT_ROOT / "Solutions"
TESTCASES_DIR = PROJECT_ROOT / "TestCases"
INPUTS_DIR = TESTCASES_DIR / "Inputs"
OUTPUTS_DIR = TESTCASES_DIR / "Outputs"
SOLUTION_CPP_PATH = SOLUTIONS_DIR / SOLUTION_CPP_NAME
# ตั้งชื่อไฟล์ executable สำหรับโจทย์นี้โดยเฉพาะ
SOLUTION_EXE_PATH = SOLUTIONS_DIR / "serenityfrostfire_solution"

def generate_one_person_data(N_val):
    """Generates a dataset for one person with a clear best-fit 's'."""
    true_s = random.randint(1, 4)
    # Use reasonable coefficients
    true_e = random.uniform(0.1, 10.0)
    true_c = random.uniform(5.0, 50.0)

    # Generate N unique n_i values to avoid division by zero
    n_values = random.sample(range(1, 150), N_val)
    d_values = []

    for n in n_values:
        perfect_d = true_e * math.pow(n, true_s) + true_c
        # Add a small noise to simulate interference
        noise = perfect_d * random.uniform(-0.001, 0.001)
        final_d = perfect_d + noise
        d_values.append(final_d)

    return n_values, d_values

def generate_input(test_case_number):
    """
    ฟังก์ชันสำหรับสร้างข้อมูล input สำหรับโจทย์ "Serenity Frostfire"
    """
    random.seed(test_case_number)

    if test_case_number <= 3: # Test each 's' value
        T = 1
    elif 4 <= test_case_number <= 7: # Mid-range T
        T = random.randint(4, 7)
    else: # Max T
        T = 10

    lines = [str(T)]

    for _ in range(T):
        N = random.randint(15, 100)
        n_vals, d_vals = generate_one_person_data(N)

        lines.append(str(N))
        lines.append(" ".join(map(str, n_vals)))
        lines.append(" ".join(f"{d:.6f}" for d in d_vals))

    return "\n".join(lines) + "\n"

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <case_num_start> [case_num_end]", file=sys.stderr)
        sys.exit(1)
    try:
        start_case = int(sys.argv[1])
        end_case = int(sys.argv[2]) if len(sys.argv) > 2 else start_case
    except ValueError:
        print("Error: Case numbers must be integers.", file=sys.stderr)
        sys.exit(1)

    INPUTS_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)

    try:
        subprocess.run(
            ["g++", str(SOLUTION_CPP_PATH), "-std=c++17", "-O2", "-o", str(SOLUTION_EXE_PATH)],
            check=True, capture_output=True, text=True
        )
    except subprocess.CalledProcessError as e:
        print("ERROR: Compilation failed!", file=sys.stderr)
        print(e.stderr, file=sys.stderr)
        sys.exit(1)

    for i in range(start_case, end_case + 1):
        input_data = generate_input(i)
        input_file_path = INPUTS_DIR / f"input{i:02d}.txt"
        with open(input_file_path, "w", encoding='utf-8') as f:
            f.write(input_data)

        output_file_path = OUTPUTS_DIR / f"output{i:02d}.txt"
        try:
            with open(output_file_path, "w", encoding='utf-8') as out_f:
                subprocess.run(
                    [str(SOLUTION_EXE_PATH)],
                    input=input_data.encode('utf-8'),
                    stdout=out_f,
                    check=True
                )
        except subprocess.CalledProcessError:
            print(f"ERROR: Solution failed on test case {i:02d}!", file=sys.stderr)
            if output_file_path.exists(): output_file_path.unlink()
            sys.exit(1)

    if start_case == end_case:
        print(f"Successfully generated test case {start_case:02d}.")
    else:
        print(f"Successfully generated test cases {start_case:02d} to {end_case:02d}.")

if __name__ == "__main__":
    main()
