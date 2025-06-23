import sys
import random
import subprocess
from pathlib import Path

# --- Configuration ---
SOLUTION_CPP_NAME = "IceCreamFestival.cpp"

# --- Path Setup ---
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
SOLUTIONS_DIR = PROJECT_ROOT / "Solutions"
TESTCASES_DIR = PROJECT_ROOT / "TestCases"
INPUTS_DIR = TESTCASES_DIR / "Inputs"
OUTPUTS_DIR = TESTCASES_DIR / "Outputs"
SOLUTION_CPP_PATH = SOLUTIONS_DIR / SOLUTION_CPP_NAME
# ตั้งชื่อไฟล์ executable สำหรับโจทย์นี้โดยเฉพาะ
SOLUTION_EXE_PATH = SOLUTIONS_DIR / "icecreamfestival_solution"


def generate_input(test_case_number):
    """
    ฟังก์ชันสำหรับสร้างข้อมูล input สำหรับโจทย์ "เทศกาลไอศกรีม (Ice Cream Festival)"
    """
    random.seed(test_case_number)

    # Subtask 1: N, M <= 50
    if 0 <= test_case_number <= 5:
        N = random.randint(40, 50)
        M = random.randint(40, 50)
        T = random.randint(0, M)
    # Subtask 2: Full constraints
    else:
        N = random.randint(9 * 10**4, 10**5)
        M = random.randint(9 * 10**3, 10**4)
        T = random.randint(M // 2, M)

    # Generate customer demands
    # Using a smaller range for demands to keep numbers reasonable
    customer_demands = [random.randint(1, 100) for _ in range(N)]

    # Generate booth closing events
    # Ensure we don't try to close the same booth twice
    available_booths = list(range(1, M + 1))
    random.shuffle(available_booths)
    closing_events = []

    # Make sure T is not greater than M
    T = min(T, M)

    for i in range(T):
        booth_to_close = available_booths[i]
        # Max customers per booth is roughly N/M. Y should be less than that.
        max_served = (N // M) + 5
        customers_to_serve = random.randint(0, max_served)
        closing_events.append((booth_to_close, customers_to_serve))

    # Build the final input string
    lines = []
    lines.append(f"{N} {M}")
    lines.append(" ".join(map(str, customer_demands)))
    lines.append(str(T))
    for event in closing_events:
        lines.append(f"{event[0]} {event[1]}")

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
