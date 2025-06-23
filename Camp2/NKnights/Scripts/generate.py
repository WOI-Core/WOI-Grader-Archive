import sys
import random
import subprocess
from pathlib import Path

# --- Configuration ---
SOLUTION_CPP_NAME = "NKnights.cpp"

# --- Path Setup ---
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
SOLUTIONS_DIR = PROJECT_ROOT / "Solutions"
TESTCASES_DIR = PROJECT_ROOT / "TestCases"
INPUTS_DIR = TESTCASES_DIR / "Inputs"
OUTPUTS_DIR = TESTCASES_DIR / "Outputs"
SOLUTION_CPP_PATH = SOLUTIONS_DIR / SOLUTION_CPP_NAME
# ตั้งชื่อไฟล์ executable สำหรับโจทย์นี้โดยเฉพาะ
SOLUTION_EXE_PATH = SOLUTIONS_DIR / "nknights_solution"


def generate_input(test_case_number):
    """
    ฟังก์ชันสำหรับสร้างข้อมูล input สำหรับโจทย์ "อัศวิน (N-Knights)"
    """
    random.seed(test_case_number)

    # Case 0: Sample 1 from PDF (N=8)
    if test_case_number == 0:
        return "8\n6 4 2 8 5 1 10 5\n9 9 3 5 6 6 2 8\n2 6 3 8 7 2 5 3\n4 3 3 2 7 9 6 8\n7 2 9 10 3 8 10 6\n5 4 2 3 4 4 5 2\n2 4 9 8 5 3 8 8\n10 4 2 10 9 7 6 1\n"
    # Case 1: Sample 2 from PDF (N=4)
    elif test_case_number == 1:
        return "4\n10 10 15 30\n20 40 100 20\n30 40 10 100\n100 10 20 30\n"

    # Test cases for various N within the constraints
    elif 2 <= test_case_number <= 4: # Very small N
        N = test_case_number # N = 2, 3, 4
    elif 5 <= test_case_number <= 9: # Mid-range N
        N = test_case_number # N = 5, 6, 7, 8, 9
    else: # Max N
        N = 10

    # Generate grid values
    min_v, max_v = 1, 40000
    grid = [[random.randint(min_v, max_v) for _ in range(N)] for _ in range(N)]

    # Build the final input string
    lines = [str(N)]
    for row in grid:
        lines.append(" ".join(map(str, row)))

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
