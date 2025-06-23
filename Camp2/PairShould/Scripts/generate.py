import sys
import random
import subprocess
from pathlib import Path

# --- Configuration ---
SOLUTION_CPP_NAME = "PairShould.cpp"

# --- Path Setup ---
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
SOLUTIONS_DIR = PROJECT_ROOT / "Solutions"
TESTCASES_DIR = PROJECT_ROOT / "TestCases"
INPUTS_DIR = TESTCASES_DIR / "Inputs"
OUTPUTS_DIR = TESTCASES_DIR / "Outputs"
SOLUTION_CPP_PATH = SOLUTIONS_DIR / SOLUTION_CPP_NAME
# ตั้งชื่อไฟล์ executable สำหรับโจทย์นี้โดยเฉพาะ
SOLUTION_EXE_PATH = SOLUTIONS_DIR / "pairshould_solution"


def generate_input(test_case_number):
    """
    ฟังก์ชันสำหรับสร้างข้อมูล input สำหรับโจทย์ "คู่ควร (Pair Should)"
    """
    random.seed(test_case_number)

    # Case 0: Sample 1 from PDF
    if test_case_number == 0:
        return "5 3\n1 1 1 1 1\n"
    # Case 1: Sample 2 from PDF
    elif test_case_number == 1:
        return "1 -200\n100\n"

    # Subtask 1: N <= 20
    elif 2 <= test_case_number <= 4:
        N = random.randint(18, 20)
        K = random.randint(-50, 50)
        A = [random.randint(0, 5) for _ in range(N)]

    # Subtask 2: All A_i are equal
    elif 5 <= test_case_number <= 7:
        N = random.randint(900, 1000)
        a_val = random.randint(1, 2) # To keep total sum in check
        A = [a_val] * N
        K = random.randint(-100, 100)

    # Subtask 3: Full constraints
    else:
        N = random.randint(950, 1000)
        K = random.randint(-2000, 2000)

        # Generate A such that sum(A) <= 2000
        A = []
        current_sum = 0
        max_sum = 2000
        for _ in range(N):
            remaining_sum = max_sum - current_sum
            max_val = min(5, remaining_sum)
            if max_val < 0: break
            val = random.randint(0, max_val)
            A.append(val)
            current_sum += val
        N = len(A) # Update N if it was cut short

    # Build the final input string
    lines = [f"{N} {K}", " ".join(map(str, A))]

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
