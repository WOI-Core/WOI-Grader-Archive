import sys
import random
import subprocess
from pathlib import Path

# --- Configuration ---
SOLUTION_CPP_NAME = "DuckBoat.cpp"

# --- Path Setup ---
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
SOLUTIONS_DIR = PROJECT_ROOT / "Solutions"
TESTCASES_DIR = PROJECT_ROOT / "TestCases"
INPUTS_DIR = TESTCASES_DIR / "Inputs"
OUTPUTS_DIR = TESTCASES_DIR / "Outputs"
SOLUTION_CPP_PATH = SOLUTIONS_DIR / SOLUTION_CPP_NAME
# ตั้งชื่อไฟล์ executable สำหรับโจทย์นี้โดยเฉพาะ
SOLUTION_EXE_PATH = SOLUTIONS_DIR / "duckboat_solution"


def generate_input(test_case_number):
    """
    ฟังก์ชันสำหรับสร้างข้อมูล input สำหรับโจทย์ "ขี่เรือเป็ด (Duck Boat)"
    """
    random.seed(test_case_number)

    N, W = 0, 0
    weights = []

    # Cases 0-1: Sample cases from PDF
    if test_case_number == 0:
        N, W = 4, 60
        weights = [20, 30, 40, 30]
    elif test_case_number == 1:
        N, W = 4, 60
        weights = [20, 50, 40, 30]

    # Subtask 1: N <= 2 * 10^3
    elif 2 <= test_case_number <= 5:
        N = random.randint(1500, 2 * 10**3)
        W = random.randint(10**8, 10**9)
        weights = [random.randint(1, W) for _ in range(N)]

    # Subtask 2: N <= 2 * 10^4
    elif 6 <= test_case_number <= 10:
        N = random.randint(15000, 2 * 10**4)
        W = random.randint(10**8, 10**9)
        weights = [random.randint(1, W // 2) for _ in range(N)] # Make pairing more likely

    # Subtask 3: Full Constraints (N <= 2*10^5) and Stress cases
    else:
        N = 2 * 10**5
        W = 10**9
        if test_case_number == 11: # No one can be paired
            # All weights are just over W/2
            min_w = (W // 2) + 1
            weights = [random.randint(min_w, W) for _ in range(N)]
        elif test_case_number == 12: # Everyone can be paired perfectly
            # All weights are exactly W/2
            # Ensure N is even for perfect pairing
            if N % 2 != 0: N -=1
            w = W // 2
            weights = [w] * N
        elif test_case_number == 13: # A mix of very light and very heavy
            light_count = N // 2
            heavy_count = N - light_count
            weights.extend([random.randint(1, W // 100) for _ in range(light_count)])
            weights.extend([random.randint(W - (W // 100), W) for _ in range(heavy_count)])
            random.shuffle(weights)
        elif test_case_number == 14: # N is odd
             if N % 2 == 0: N -=1
             weights = [random.randint(1, W) for _ in range(N)]
        else: # Random max case
             weights = [random.randint(1, W) for _ in range(N)]

    # สร้าง String output
    input_lines = [f"{N} {W}", " ".join(map(str, weights))]
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
