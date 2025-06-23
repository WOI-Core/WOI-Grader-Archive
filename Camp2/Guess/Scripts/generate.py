import sys
import random
import subprocess
from pathlib import Path

# --- Configuration ---
SOLUTION_CPP_NAME = "Guess.cpp"

# --- Path Setup ---
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
SOLUTIONS_DIR = PROJECT_ROOT / "Solutions"
TESTCASES_DIR = PROJECT_ROOT / "TestCases"
INPUTS_DIR = TESTCASES_DIR / "Inputs"
OUTPUTS_DIR = TESTCASES_DIR / "Outputs"
SOLUTION_CPP_PATH = SOLUTIONS_DIR / SOLUTION_CPP_NAME
# ตั้งชื่อไฟล์ executable สำหรับโจทย์นี้โดยเฉพาะ
SOLUTION_EXE_PATH = SOLUTIONS_DIR / "guess_solution"


def calculate_ph(secret, guess):
    """
    Calculates the number of correct positions (pos) and correct digits in wrong positions (have).
    """
    pos = 0
    have = 0
    n = len(secret)
    secret_counts = {}
    guess_counts = {}

    # Calculate positions
    for i in range(n):
        if secret[i] == guess[i]:
            pos += 1
        else:
            secret_counts[secret[i]] = secret_counts.get(secret[i], 0) + 1
            guess_counts[guess[i]] = guess_counts.get(guess[i], 0) + 1

    # Calculate haves
    for digit, count in guess_counts.items():
        if digit in secret_counts:
            have += min(count, secret_counts[digit])

    return pos, have


def generate_input(test_case_number):
    """
    ฟังก์ชันสำหรับสร้างข้อมูล input สำหรับโจทย์ "เกมทายตัวเลข (Guess)"
    """
    random.seed(test_case_number)

    # Cases 0-1: Sample cases from PDF
    if test_case_number == 0: #
        return "5 4\n3 4 5 7 1 2 2\n9 1 3 6 8 1 2\n3 5 7 2 8 1 1\n9 3 8 5 6 3 0\n"
    elif test_case_number == 1: #
        return "3 2\n8 3 9 1 0\n1 2 7 1 1\n"

    # Since N digits must be unique from 1-9, N cannot exceed 9.
    if test_case_number < 12:
        N = random.randint(3, 8)
        M = random.randint(2, 7)
    else: # Max case
        N = 9
        M = 10

    # Generate a secret number
    all_digits = list(range(1, 10))
    secret = random.sample(all_digits, N)

    conditions = []
    for _ in range(M):
        guess = random.sample(all_digits, N)
        pos, have = calculate_ph(secret, guess)
        condition_line = " ".join(map(str, guess)) + f" {pos} {have}"
        conditions.append(condition_line)

    # Build the final input string
    header = f"{N} {M}"
    full_input = [header] + conditions
    return "\n".join(full_input) + "\n"


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
