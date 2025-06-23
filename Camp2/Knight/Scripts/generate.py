import sys
import random
import subprocess
from pathlib import Path

# --- Configuration ---
SOLUTION_CPP_NAME = "Knight.cpp"

# --- Path Setup ---
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
SOLUTIONS_DIR = PROJECT_ROOT / "Solutions"
TESTCASES_DIR = PROJECT_ROOT / "TestCases"
INPUTS_DIR = TESTCASES_DIR / "Inputs"
OUTPUTS_DIR = TESTCASES_DIR / "Outputs"
SOLUTION_CPP_PATH = SOLUTIONS_DIR / SOLUTION_CPP_NAME
# ตั้งชื่อไฟล์ executable สำหรับโจทย์นี้โดยเฉพาะ
SOLUTION_EXE_PATH = SOLUTIONS_DIR / "knight_solution"


def generate_input(test_case_number):
    """
    ฟังก์ชันสำหรับสร้างข้อมูล input สำหรับโจทย์ "อัศวินเดิน (Knight)"
    """
    random.seed(test_case_number)

    N, x, y, a, b = 0, 0, 0, 0, 0

    # Case 0-1: Sample cases from PDF
    if test_case_number == 0:
        N, x, y, a, b = 7, 1, 1, 4, 4
    elif test_case_number == 1:
        N, x, y, a, b = 10, 10, 10, 1, 1

    # Edge Cases
    elif test_case_number == 2: # Start == Target
        N = 100
        a = b = x = y = random.randint(1, N)
    elif test_case_number == 3: # One move away
        N = 100
        a, b = 50, 50
        moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        move = random.choice(moves)
        x, y = a + move[0], b + move[1]
    elif test_case_number == 4: # Small board (5x5), corner to corner
        N = 5
        a, b = 1, 1
        x, y = 5, 5
    elif test_case_number == 5: # Small board, unreachable test (e.g. 2x2 board)
        N = 2
        a, b = 1, 1
        x, y = 1, 2 # unreachable

    # Max Constraint Cases
    else:
        N = 1000
        if test_case_number == 6: # Corner to opposite corner
            a, b = 1, 1
            x, y = N, N
        elif test_case_number == 7: # Corner to adjacent corner
            a, b = 1, 1
            x, y = 1, N
        else: # Random max case
            a = random.randint(1, N)
            b = random.randint(1, N)
            x = random.randint(1, N)
            y = random.randint(1, N)

    # Build the final input string
    lines = [str(N), f"{x} {y}", f"{a} {b}"]
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
            if output_file_path.exists():
                output_file_path.unlink()
            sys.exit(1)

    if start_case == end_case:
        print(f"Successfully generated test case {start_case:02d}.")
    else:
        print(f"Successfully generated test cases {start_case:02d} to {end_case:02d}.")

if __name__ == "__main__":
    main()
