import sys
import random
import subprocess
from pathlib import Path

# --- Configuration ---
SOLUTION_CPP_NAME = "Anonymous.cpp"

# --- Path Setup ---
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
SOLUTIONS_DIR = PROJECT_ROOT / "Solutions"
TESTCASES_DIR = PROJECT_ROOT / "TestCases"
INPUTS_DIR = TESTCASES_DIR / "Inputs"
OUTPUTS_DIR = TESTCASES_DIR / "Outputs"
SOLUTION_CPP_PATH = SOLUTIONS_DIR / SOLUTION_CPP_NAME
SOLUTION_EXE_PATH = SOLUTIONS_DIR / "anonymous_solution"


def generate_input(test_case_number):
    """
    ฟังก์ชันสำหรับ "สร้างข้อมูล" ของ test case แต่ละอัน
    จะ return เป็น string ของข้อมูล input แทนการ print ออกมา
    """
    random.seed(test_case_number)
    lines = []
    # Cases 0-1: Sample cases from PDF
    if test_case_number == 0:
        lines.extend(["3", "2", "3", "4"])
    elif test_case_number == 1:
        lines.extend(["2", "200000000", "199999991"])
    # Subtask 1: 1 <= Q <= 100, 2 <= N <= 100
    elif 2 <= test_case_number <= 5:
        Q = random.randint(50, 100)
        lines.append(str(Q))
        for _ in range(Q):
            lines.append(str(random.randint(2, 100)))
    # Subtask 2: 1 <= Q <= 10^4, 2 <= N <= 10^6
    elif 6 <= test_case_number <= 10:
        Q = random.randint(9000, 10**4)
        lines.append(str(Q))
        for _ in range(Q):
            lines.append(str(random.randint(100, 10**6)))
    # Subtask 3: N <= 10^7, Q = 1
    elif 11 <= test_case_number <= 13:
        Q = 1
        lines.append(str(Q))
        if test_case_number == 11: N = 10**7
        elif test_case_number == 12: N = random.randint(10**6, 10**7)
        else: N = 9999991
        lines.append(str(N))
    # Subtask 4: 1 <= Q <= 3*10^4, 2 <= N <= 10^7
    elif 14 <= test_case_number <= 18:
        Q = random.randint(28000, 3 * 10**4)
        lines.append(str(Q))
        for _ in range(Q):
            lines.append(str(random.randint(10**6, 10**7)))
    # Subtask 5: Full Constraints
    elif 19 <= test_case_number <= 30:
        Q = 3 * 10**4
        max_n = 2 * 10**8
        lines.append(str(Q))
        if test_case_number == 19:
            for _ in range(Q): lines.append(str(random.randint(max_n - 1000, max_n)))
        elif test_case_number == 20:
            for _ in range(Q): lines.append(str(max_n))
        else:
            for _ in range(Q): lines.append(str(random.randint(2, max_n)))
    return "\n".join(lines) + "\n"

def main():
    # --- 1. Argument Parsing ---
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <case_num_start> [case_num_end]", file=sys.stderr)
        sys.exit(1)
    try:
        start_case = int(sys.argv[1])
        end_case = int(sys.argv[2]) if len(sys.argv) > 2 else start_case
    except ValueError:
        print("Error: Case numbers must be integers.", file=sys.stderr)
        sys.exit(1)

    # --- 2. Setup Directories and Compile ---
    INPUTS_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)

    try:
        # การคอมไพล์ยังคงทำงานเหมือนเดิม แต่ไม่แสดงผลลัพธ์
        subprocess.run(
            ["g++", str(SOLUTION_CPP_PATH), "-std=c++17", "-O2", "-o", str(SOLUTION_EXE_PATH)],
            check=True, capture_output=True, text=True
        )
    except subprocess.CalledProcessError as e:
        print("ERROR: Compilation failed!", file=sys.stderr)
        print(e.stderr, file=sys.stderr)
        sys.exit(1)

    # --- 3. Generation Loop ---
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
                output_file_path.unlink() # ลบไฟล์ output ที่อาจสร้างไม่สมบูรณ์
            sys.exit(1)

    # --- 4. Final Success Message ---
    if start_case == end_case:
        print(f"Successfully generated test case {start_case:02d}.")
    else:
        print(f"Successfully generated test cases {start_case:02d} to {end_case:02d}.")

if __name__ == "__main__":
    main()
