import sys
import random
import subprocess
from pathlib import Path

# --- Configuration ---
SOLUTION_CPP_NAME = "CountWall.cpp"

# --- Path Setup ---
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
SOLUTIONS_DIR = PROJECT_ROOT / "Solutions"
TESTCASES_DIR = PROJECT_ROOT / "TestCases"
INPUTS_DIR = TESTCASES_DIR / "Inputs"
OUTPUTS_DIR = TESTCASES_DIR / "Outputs"
SOLUTION_CPP_PATH = SOLUTIONS_DIR / SOLUTION_CPP_NAME
# ตั้งชื่อไฟล์ executable สำหรับโจทย์นี้โดยเฉพาะ
SOLUTION_EXE_PATH = SOLUTIONS_DIR / "countwall_solution"


def generate_input(test_case_number):
    """
    ฟังก์ชันสำหรับสร้างข้อมูล input สำหรับโจทย์ "นับกำแพง (CountWall)"
    """
    random.seed(test_case_number)

    R, C = 0, 0
    grid = []

    # Cases 0-1: Sample cases from PDF
    if test_case_number == 0:
        R, C = 4, 5
        # The PDF shows non-space-separated input, but the C++ solution
        # expects space-separated. We generate for the C++ solution.
        grid_str = ["00000", "01000", "01100", "00010"]
        grid = [[int(c) for c in row] for row in grid_str]
    elif test_case_number == 1:
        R, C = 6, 6
        grid_str = ["000000", "011000", "011001", "000010", "110010", "010110"]
        grid = [[int(c) for c in row] for row in grid_str]

    # Subtask 1: R, C <= 200
    elif 2 <= test_case_number <= 5:
        R = random.randint(150, 200)
        C = random.randint(150, 200)
        # 30% chance of being land
        grid = [[(1 if random.random() < 0.3 else 0) for _ in range(C)] for _ in range(R)]

    # Subtask 2: R, C <= 300
    elif 6 <= test_case_number <= 10:
        R = random.randint(250, 300)
        C = random.randint(250, 300)
        # 50% chance of being land
        grid = [[(1 if random.random() < 0.5 else 0) for _ in range(C)] for _ in range(R)]

    # Subtask 3: Full Constraints (R, C <= 600) and Stress cases
    else:
        R, C = 600, 600
        if test_case_number == 11: # All sea
            grid = [[0] * C for _ in range(R)]
        elif test_case_number == 12: # All land
            grid = [[1] * C for _ in range(R)]
        elif test_case_number == 13: # Checkerboard pattern
            grid = [[(i + j) % 2 for j in range(C)] for i in range(R)]
        elif test_case_number == 14: # Single land in the middle
             grid = [[0] * C for _ in range(R)]
             grid[R//2][C//2] = 1
        else: # Random max case
             grid = [[(1 if random.random() < 0.5 else 0) for _ in range(C)] for _ in range(R)]


    # สร้าง String output
    # First line: R and C
    input_lines = [f"{R} {C}"]
    # Following R lines: the grid, with space-separated values
    for row in grid:
        input_lines.append(" ".join(map(str, row)))

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
