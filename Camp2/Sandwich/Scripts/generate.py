import sys
import random
import subprocess
from pathlib import Path

# --- Configuration ---
SOLUTION_CPP_NAME = "Sandwich.cpp"

# --- Path Setup ---
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
SOLUTIONS_DIR = PROJECT_ROOT / "Solutions"
TESTCASES_DIR = PROJECT_ROOT / "TestCases"
INPUTS_DIR = TESTCASES_DIR / "Inputs"
OUTPUTS_DIR = TESTCASES_DIR / "Outputs"
SOLUTION_CPP_PATH = SOLUTIONS_DIR / SOLUTION_CPP_NAME
# ตั้งชื่อไฟล์ executable สำหรับโจทย์นี้โดยเฉพาะ
SOLUTION_EXE_PATH = SOLUTIONS_DIR / "sandwich_solution"


def generate_input(test_case_number):
    """
    ฟังก์ชันสำหรับสร้างข้อมูล input สำหรับโจทย์ "แซนด์วิช (Sandwich)"
    """
    random.seed(test_case_number)

    # Subtask 1
    if 0 <= test_case_number <= 2:
        N = random.randint(900, 1000)
        Q = random.randint(90, 100)
    # Subtask 2
    elif 3 <= test_case_number <= 5:
        N = random.randint(9000, 10000)
        Q = random.randint(900, 1000)
    # Subtask 3
    elif 6 <= test_case_number <= 8:
        N = random.randint(90000, 100000)
        Q = random.randint(9000, 10000)
    # Subtask 4 (Full constraints)
    else:
        # Cap at 2e5 to keep file sizes and generation time reasonable
        N = random.randint(180000, 200000)
        Q = random.randint(180000, 200000)

    # Generate sandwich values
    min_s, max_s = -1000, 1000
    s_values = [random.randint(min_s, max_s) for _ in range(N)]

    # Generate queries
    max_m = 2 * 10**6
    queries = []
    for _ in range(Q):
        p = random.randint(1, N)
        m = random.randint(1, max_m)
        queries.append(f"{p} {m}")

    # Build the final input string
    lines = [f"{N}"]
    lines.append(" ".join(map(str, s_values)))
    lines.append(str(Q))
    lines.extend(queries)

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
