import sys
import random
import subprocess
from pathlib import Path

# --- Configuration ---
SOLUTION_CPP_NAME = "Flood.cpp"

# --- Path Setup ---
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
SOLUTIONS_DIR = PROJECT_ROOT / "Solutions"
TESTCASES_DIR = PROJECT_ROOT / "TestCases"
INPUTS_DIR = TESTCASES_DIR / "Inputs"
OUTPUTS_DIR = TESTCASES_DIR / "Outputs"
SOLUTION_CPP_PATH = SOLUTIONS_DIR / SOLUTION_CPP_NAME
# ตั้งชื่อไฟล์ executable สำหรับโจทย์นี้โดยเฉพาะ
SOLUTION_EXE_PATH = SOLUTIONS_DIR / "flood_solution"


def generate_input(test_case_number):
    """
    ฟังก์ชันสำหรับสร้างข้อมูล input สำหรับโจทย์ "น้ำท่วม (Flood)"
    """
    random.seed(test_case_number)

    N, V = 0, 0
    heights = []

    # Cases 0-1: Sample cases from PDF (Note: these do not meet problem constraints)
    if test_case_number == 0:
        N, V = 6, 17
        heights = [2, 5, 1, 3, 6, 4]
    elif test_case_number == 1:
        N, V = 5, 12
        heights = [5, 1, 3, 5, 2]

    # Full constraint cases (10^4 <= N <= 10^5, 10^4 <= V <= 1.5*10^6, 1 <= h <= 40)
    else:
        min_n, max_n = 10**4, 10**5
        min_v, max_v = 10**4, 15 * 10**5
        min_h, max_h = 1, 40

        if test_case_number == 2: # Min N, Min V
            N = min_n
            V = min_v
            heights = [random.randint(min_h, max_h) for _ in range(N)]
        elif test_case_number == 3: # Max N, Max V
            N = max_n
            V = max_v
            heights = [random.randint(min_h, max_h) for _ in range(N)]
        elif test_case_number == 4: # All heights are the same
            N = random.randint(min_n, max_n)
            V = random.randint(min_v, max_v)
            h = random.randint(min_h, max_h)
            heights = [h] * N
        elif test_case_number == 5: # All heights are max
            N = random.randint(min_n, max_n)
            V = max_v # Use large volume
            heights = [max_h] * N
        elif test_case_number == 6: # All heights are min
            N = random.randint(min_n, max_n)
            V = min_v # Use small volume
            heights = [min_h] * N
        else: # Random case within full constraints
            N = random.randint(min_n, max_n)
            V = random.randint(min_v, max_v)
            heights = [random.randint(min_h, max_h) for _ in range(N)]

    # สร้าง String output
    # First line: N and V
    input_lines = [f"{N} {V}"]
    # Following N lines: each height on a new line
    input_lines.extend(map(str, heights))

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
