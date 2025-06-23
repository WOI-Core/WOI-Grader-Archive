import sys
import random
import subprocess
from pathlib import Path

# --- Configuration ---
SOLUTION_CPP_NAME = "LumpineeTreasure.cpp"

# --- Path Setup ---
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
SOLUTIONS_DIR = PROJECT_ROOT / "Solutions"
TESTCASES_DIR = PROJECT_ROOT / "TestCases"
INPUTS_DIR = TESTCASES_DIR / "Inputs"
OUTPUTS_DIR = TESTCASES_DIR / "Outputs"
SOLUTION_CPP_PATH = SOLUTIONS_DIR / SOLUTION_CPP_NAME
# ตั้งชื่อไฟล์ executable สำหรับโจทย์นี้โดยเฉพาะ
SOLUTION_EXE_PATH = SOLUTIONS_DIR / "lumpineetreasure_solution"


def generate_input(test_case_number):
    """
    ฟังก์ชันสำหรับสร้างข้อมูล input สำหรับโจทย์ "Lumpinee Treasure"
    NOTE: The provided solution is a slow brute-force recursion.
    N, M, and especially K must be kept small to avoid Time Limit Exceeded.
    The C++ code uses arr[11][11], so we will cap N, M at 10.
    """
    random.seed(test_case_number)

    # Case 0-1: Sample cases from PDF
    if test_case_number == 0:
        return "5 5 2\n0 1 0 2 0\n3 0 3 0 0\n0 0 0 0 0\n0 0 0 4 5\n0 3 0 1 0\n"
    elif test_case_number == 1:
        return "5 4 7\n9 0 0 0\n0 0 1 5\n0 0 0 0\n0 0 12 0\n0 0 0 0\n"

    # Small cases that the brute-force solution can handle
    else:
        # Cap N, M at 10 as hinted by the C++ code's array size
        N = random.randint(5, 10)
        M = random.randint(5, 10)
        # Cap K to a value that is not too slow for 2^K complexity
        K = random.randint(8, 16)

    # Generate grid values
    min_v, max_v = 1, 150
    grid = [[random.randint(min_v, max_v) for _ in range(M)] for _ in range(N)]

    # Build the final input string
    lines = [f"{N} {M} {K}"]
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
                    check=True,
                    timeout=1.0 # Add a timeout to prevent it from running too long
                )
        except subprocess.TimeoutExpired:
            print(f"ERROR: Solution timed out on test case {i:02d}!", file=sys.stderr)
            if output_file_path.exists(): output_file_path.unlink()
            sys.exit(1)
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
