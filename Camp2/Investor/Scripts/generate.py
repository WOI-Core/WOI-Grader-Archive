import sys
import random
import subprocess
from pathlib import Path

# --- Configuration ---
SOLUTION_CPP_NAME = "investor.cpp"

# --- Path Setup ---
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
SOLUTIONS_DIR = PROJECT_ROOT / "Solutions"
TESTCASES_DIR = PROJECT_ROOT / "TestCases"
INPUTS_DIR = TESTCASES_DIR / "Inputs"
OUTPUTS_DIR = TESTCASES_DIR / "Outputs"
SOLUTION_CPP_PATH = SOLUTIONS_DIR / SOLUTION_CPP_NAME
# ตั้งชื่อไฟล์ executable สำหรับโจทย์นี้โดยเฉพาะ
SOLUTION_EXE_PATH = SOLUTIONS_DIR / "investor_solution"


def generate_input(test_case_number):
    """
    ฟังก์ชันสำหรับสร้างข้อมูล input สำหรับโจทย์ "นักลงทุน (Investor)"
    """
    random.seed(test_case_number)

    # Subtask 1 & 2: N, Q <= 2e4, Commands A and C only
    if 0 <= test_case_number <= 2:
        N = random.randint(15000, 2 * 10**4)
        Q = random.randint(15000, 2 * 10**4)
        commands = ['A', 'C']
    # Subtask 3: N, Q <= 2e4, All commands
    elif 3 <= test_case_number <= 5:
        N = random.randint(15000, 2 * 10**4)
        Q = random.randint(15000, 2 * 10**4)
        commands = ['A', 'B', 'C', 'D']
    # Subtask 4 & 5: Full constraints N, Q <= 2e5
    else:
        N = random.randint(18 * 10**4, 2 * 10**5)
        Q = random.randint(18 * 10**4, 2 * 10**5)
        commands = ['A', 'B', 'C', 'D']

    # Generate initial values
    initial_values = [random.randint(1, 1000) for _ in range(N)]

    # Generate Q commands
    query_lines = []
    # Special case: create long chains and test repeated merges
    if test_case_number > 5 and test_case_number % 3 == 0:
        # Many merges first
        for _ in range(Q // 2):
             x = random.randint(1, N)
             y = random.randint(1, N)
             query_lines.append(f"A {x} {y}")
        # Then queries
        for _ in range(Q - (Q // 2)):
             cmd = random.choice(commands[1:]) # B, C, or D
             node = random.randint(1, N)
             query_lines.append(f"{cmd} {node}")
    else: # Random commands
        for _ in range(Q):
            cmd = random.choice(commands)
            if cmd == 'A':
                x = random.randint(1, N)
                y = random.randint(1, N)
                query_lines.append(f"A {x} {y}")
            else: # B, C, D
                node = random.randint(1, N)
                query_lines.append(f"{cmd} {node}")

    # Build the final input string
    lines = []
    lines.append(f"{N} {Q}")
    lines.append(" ".join(map(str, initial_values)))
    lines.extend(query_lines)

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
