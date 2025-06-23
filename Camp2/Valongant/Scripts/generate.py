import sys
import random
import subprocess
from pathlib import Path

# --- Configuration ---
SOLUTION_CPP_NAME = "Valongant.cpp"

# --- Path Setup ---
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
SOLUTIONS_DIR = PROJECT_ROOT / "Solutions"
TESTCASES_DIR = PROJECT_ROOT / "TestCases"
INPUTS_DIR = TESTCASES_DIR / "Inputs"
OUTPUTS_DIR = TESTCASES_DIR / "Outputs"
SOLUTION_CPP_PATH = SOLUTIONS_DIR / SOLUTION_CPP_NAME
# ตั้งชื่อไฟล์ executable สำหรับโจทย์นี้โดยเฉพาะ
SOLUTION_EXE_PATH = SOLUTIONS_DIR / "valongant_solution"


def generate_input(test_case_number):
    """
    ฟังก์ชันสำหรับสร้างข้อมูล input สำหรับโจทย์ "วาโลแง็น (VALONGANT)"
    """
    random.seed(test_case_number)

    # Sample 1
    if test_case_number == 0:
        return "6 8\n0 1 11\n0 3 10\n0 4 70\n1 2 5\n2 3 1\n2 5 100\n3 4 2\n5 3 20\n"
    # Sample 2
    elif test_case_number == 1:
        return "6 8\n0 1 3\n0 2 10\n0 3 4\n1 2 2\n1 4 3\n2 3 2\n2 4 7\n3 4 6\n"

    # Since N is always small (<= 100), we vary E based on subtasks
    N = random.randint(90, 100)

    # Subtask 1
    if 2 <= test_case_number <= 4:
        E = random.randint(10**5, 10**5 + 99)
    # Subtask 2
    elif 5 <= test_case_number <= 7:
        E = random.randint(10**6, 10**6 + 99)
    # Subtask 3 (Full constraints)
    else:
        # Cap E to keep generation fast, as N is small and graph will be dense anyway
        max_possible_edges = N * (N - 1) // 2
        E = random.randint(max_possible_edges - 100, max_possible_edges)

    edges = set()
    # Ensure a path exists by creating a simple line graph first
    for i in range(N - 1):
        w = random.randint(1, 99)
        edges.add(tuple(sorted((i, i + 1))) + (w,))

    # Add random edges until we reach E
    while len(edges) < E:
        u = random.randint(0, N - 1)
        v = random.randint(0, N - 1)
        if u != v:
            w = random.randint(1, 99)
            edges.add(tuple(sorted((u, v))) + (w,))

    # Build the final input string
    lines = [f"{N} {len(edges)}"]
    for u, v, w in edges:
        lines.append(f"{u} {v} {w}")

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
