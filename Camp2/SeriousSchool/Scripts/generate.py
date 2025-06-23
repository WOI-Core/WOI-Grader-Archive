import sys
import random
import subprocess
from pathlib import Path

# --- Configuration ---
SOLUTION_CPP_NAME = "SeriousSchool.cpp"

# --- Path Setup ---
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
SOLUTIONS_DIR = PROJECT_ROOT / "Solutions"
TESTCASES_DIR = PROJECT_ROOT / "TestCases"
INPUTS_DIR = TESTCASES_DIR / "Inputs"
OUTPUTS_DIR = TESTCASES_DIR / "Outputs"
SOLUTION_CPP_PATH = SOLUTIONS_DIR / SOLUTION_CPP_NAME
# ตั้งชื่อไฟล์ executable สำหรับโจทย์นี้โดยเฉพาะ
SOLUTION_EXE_PATH = SOLUTIONS_DIR / "seriousschool_solution"


def generate_input(test_case_number):
    """
    ฟังก์ชันสำหรับสร้างข้อมูล input สำหรับโจทย์ "SeriousSchool"
    """
    random.seed(test_case_number)

    lines = []

    # Sample 1
    if test_case_number == 0:
        return "85\n4\n1 2 11\n2 2 5\n3 4 10\n6 6 6\n"
    # Sample 2
    elif test_case_number == 1:
        return "60\n6\n1 1 4\n1 2 8\n2 4 10\n6 7 12\n9 10 14\n11 14 15\n"

    # Case: Already has 100+ score
    elif test_case_number == 2:
        score = 101
        N = 10
        lines.append(str(score))
        lines.append(str(N))
        for _ in range(N):
            start = random.randint(1, 300)
            end = start + random.randint(0, 5)
            s_gain = random.randint(1, 20)
            lines.append(f"{start} {end} {s_gain}")

    # Case: Impossible to reach 100
    elif test_case_number == 3:
        score = 95
        N = 20
        lines.append(str(score))
        lines.append(str(N))
        # All activities give very few points
        for i in range(N):
            start = i * 2 + 1
            end = start
            s_gain = 0 # No points gained
            lines.append(f"{start} {end} {s_gain}")

    # General random cases
    else:
        score = random.randint(1, 80)
        N = 100
        lines.append(str(score))
        lines.append(str(N))
        # Generate N activities
        for _ in range(N):
            # Assume activities are within a year
            start = random.randint(1, 350)
            # Duration between 1 and 10 days
            duration = random.randint(0, 9)
            end = start + duration
            # Score gain between 1 and 25
            s_gain = random.randint(1, 25)
            lines.append(f"{start} {end} {s_gain}")

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
