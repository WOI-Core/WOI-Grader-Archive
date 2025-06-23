import sys
import random
import subprocess
from pathlib import Path

# --- Configuration ---
SOLUTION_CPP_NAME = "Budget.cpp"

# --- Path Setup ---
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
SOLUTIONS_DIR = PROJECT_ROOT / "Solutions"
TESTCASES_DIR = PROJECT_ROOT / "TestCases"
INPUTS_DIR = TESTCASES_DIR / "Inputs"
OUTPUTS_DIR = TESTCASES_DIR / "Outputs"
SOLUTION_CPP_PATH = SOLUTIONS_DIR / SOLUTION_CPP_NAME
# ตั้งชื่อไฟล์ executable สำหรับโจทย์นี้โดยเฉพาะ
SOLUTION_EXE_PATH = SOLUTIONS_DIR / "budget_solution"


def generate_input(test_case_number):
    """
    ฟังก์ชันสำหรับสร้างข้อมูล input สำหรับโจทย์ "ตัดงบ (Budget Cut)"
    """
    random.seed(test_case_number)

    # --- Constraints ---
    MAX_N_FULL = 3 * 10**7
    MAX_M_FULL = 10**6

    N, M_list = 0, []

    # Cases 0-2: Sample cases from PDF
    if test_case_number == 0:
        N, M_list = 3, [2, 4, 1]
    elif test_case_number == 1:
        N, M_list = 5, [1, 2, 5, 4, 3]
    elif test_case_number == 2:
        N, M_list = 10, list(range(10))

    # Subtask 1: N <= 100, M <= 500
    elif 3 <= test_case_number <= 5:
        N = random.randint(50, 100)
        M_list = [random.randint(1, 500) for _ in range(N)]

    # Subtask 3: N <= 2*10^5
    elif 6 <= test_case_number <= 10:
        N = random.randint(10**5, 2 * 10**5)
        M_list = [random.randint(1, 5 * 10**4) for _ in range(N)]

    # Subtask 4: N <= 2*10^7
    elif 11 <= test_case_number <= 15:
        N = random.randint(10**7, 2 * 10**7)
        M_list = [random.randint(0, MAX_M_FULL) for _ in range(N)]

    # Subtask 5: Full Constraints (N <= 3*10^7)
    # และ Tricky/Stress cases
    else:
        N = MAX_N_FULL
        if test_case_number == 16: # Random max
            M_list = [random.randint(0, MAX_M_FULL) for _ in range(N)]
        elif test_case_number == 17: # All same value (max pairs)
            val = random.randint(0, MAX_M_FULL)
            M_list = [val] * N
        elif test_case_number == 18: # Strictly increasing (0 pairs)
            # To avoid exceeding max M, we start from 0
            M_list = list(range(N)) if N <= MAX_M_FULL + 1 else [random.randint(0, MAX_M_FULL)] * N
        elif test_case_number == 19: # Strictly decreasing (max pairs)
            M_list = list(range(N - 1, -1, -1)) if N <= MAX_M_FULL + 1 else [random.randint(0, MAX_M_FULL)] * N
        else: # Default max case
             M_list = [random.randint(0, MAX_M_FULL) for _ in range(N)]

    # สร้าง String output
    input_lines = [str(N), " ".join(map(str, M_list))]
    return "\n".join(input_lines) + "\n"

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
            if output_file_path.exists():
                output_file_path.unlink()
            sys.exit(1)

    if start_case == end_case:
        print(f"Successfully generated test case {start_case:02d}.")
    else:
        print(f"Successfully generated test cases {start_case:02d} to {end_case:02d}.")

if __name__ == "__main__":
    main()
