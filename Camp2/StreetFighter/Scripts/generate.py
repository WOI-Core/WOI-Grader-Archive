import sys
import random
import subprocess
from pathlib import Path

# --- Configuration ---
SOLUTION_CPP_NAME = "streetfighter.cpp"

# --- Path Setup ---
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
SOLUTIONS_DIR = PROJECT_ROOT / "Solutions"
TESTCASES_DIR = PROJECT_ROOT / "TestCases"
INPUTS_DIR = TESTCASES_DIR / "Inputs"
OUTPUTS_DIR = TESTCASES_DIR / "Outputs"
SOLUTION_CPP_PATH = SOLUTIONS_DIR / SOLUTION_CPP_NAME
# ตั้งชื่อไฟล์ executable สำหรับโจทย์นี้โดยเฉพาะ
SOLUTION_EXE_PATH = SOLUTIONS_DIR / "streetfighter_solution"


def generate_input(test_case_number):
    """
    ฟังก์ชันสำหรับสร้างข้อมูล input สำหรับโจทย์ "นักสู้ข้างถนน (Street Fighter)"
    """
    random.seed(test_case_number)

    # Sample cases
    if test_case_number == 0:
        return "5 5\n10 20 30 40 50\n20 30 10 50 40\nA\nA\nA\nB\nA\n"
    elif test_case_number == 1:
        return "5 5\n10 20 30 40 50\n10 20 30 40 50\nA\nB\nA\nB\nA\n"

    # Subtask 1: N, T <= 10^3
    elif 2 <= test_case_number <= 3:
        N = random.randint(500, 1000)
        T = random.randint(500, 1000)
        commands = ['A', 'B']
    # Subtask 2: N, T <= 10^4, A only
    elif 4 <= test_case_number <= 5:
        N = random.randint(5000, 10000)
        T = random.randint(5000, 10000)
        commands = ['A']
    # Subtask 3: N, T <= 10^4
    elif 6 <= test_case_number <= 7:
        N = random.randint(5000, 10000)
        T = random.randint(5000, 10000)
        commands = ['A', 'B']
    # Subtask 4: N, T <= 10^5, A only
    elif 8 <= test_case_number <= 9:
        N = random.randint(50000, 100000)
        T = random.randint(50000, 100000)
        commands = ['A']
    # Subtask 5: Full constraints
    else:
        N = random.randint(900000, 1000000)
        T = random.randint(900000, 1000000)
        commands = ['A', 'B']

    # Generate powers
    min_p, max_p = 1, 10**6
    gang_x = [random.randint(min_p, max_p) for _ in range(N)]
    gang_y = [random.randint(min_p, max_p) for _ in range(N)]

    # Generate events
    # To avoid too many 'B' queries which slow down I/O, we weigh 'A' more heavily
    event_choices = commands * 10 if 'B' in commands else commands
    if 'A' in event_choices: event_choices.extend(['A'] * 90)

    events = [random.choice(event_choices) for _ in range(T)]

    # Build input string
    lines = [f"{N} {T}"]
    lines.append(" ".join(map(str, gang_x)))
    lines.append(" ".join(map(str, gang_y)))
    lines.extend(events)

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
                    timeout=5.0 # Increased timeout for potentially large I/O
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
