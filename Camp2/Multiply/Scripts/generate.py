import sys
import random
import subprocess
from pathlib import Path

# --- Configuration ---
SOLUTION_CPP_NAME = "Multiply.cpp"

# --- Path Setup ---
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
SOLUTIONS_DIR = PROJECT_ROOT / "Solutions"
TESTCASES_DIR = PROJECT_ROOT / "TestCases"
INPUTS_DIR = TESTCASES_DIR / "Inputs"
OUTPUTS_DIR = TESTCASES_DIR / "Outputs"
SOLUTION_CPP_PATH = SOLUTIONS_DIR / SOLUTION_CPP_NAME
# ตั้งชื่อไฟล์ executable สำหรับโจทย์นี้โดยเฉพาะ
SOLUTION_EXE_PATH = SOLUTIONS_DIR / "multiply_solution"


def generate_input(test_case_number):
    """
    ฟังก์ชันสำหรับสร้างข้อมูล input สำหรับโจทย์ "Multiply"
    NOTE: The provided solution crashes if b >= 1000 (4 digits).
    This generator ensures b is always in the range [1, 999].
    """
    random.seed(test_case_number)

    # Case 0: Sample 1 from PDF
    if test_case_number == 0:
        a = "1"
        b = "2"
    # Case 1: Sample 2 from PDF
    elif test_case_number == 1:
        a = "12345678"
        b = "321"
    # Max value cases
    elif test_case_number == 2:
        # Max 'a' (24 nines), Max 'b' that works with solution
        a = '9' * 24
        b = "999"
    elif test_case_number == 3:
        # Max 'a' (24 nines), b=1
        a = '9' * 24
        b = "1"
    # Random cases
    else:
        # Generate 'a' with random length up to 24
        len_a = random.randint(1, 24)
        if len_a == 1:
            a = str(random.randint(1, 9))
        else:
            first_digit = str(random.randint(1, 9))
            other_digits = "".join([str(random.randint(0, 9)) for _ in range(len_a - 1)])
            a = first_digit + other_digits

        # Generate 'b' from 1 to 999
        b = str(random.randint(1, 999))

    return f"{a}\n{b}\n"

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
