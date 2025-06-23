import sys
import random
import subprocess
from pathlib import Path

# --- Configuration ---
SOLUTION_CPP_NAME = "TwoTree.cpp"

# --- Path Setup ---
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
SOLUTIONS_DIR = PROJECT_ROOT / "Solutions"
TESTCASES_DIR = PROJECT_ROOT / "TestCases"
INPUTS_DIR = TESTCASES_DIR / "Inputs"
OUTPUTS_DIR = TESTCASES_DIR / "Outputs"
SOLUTION_CPP_PATH = SOLUTIONS_DIR / SOLUTION_CPP_NAME
# ตั้งชื่อไฟล์ executable สำหรับโจทย์นี้โดยเฉพาะ
SOLUTION_EXE_PATH = SOLUTIONS_DIR / "twotree_solution"


def generate_input(test_case_number):
    """
    ฟังก์ชันสำหรับสร้างข้อมูล input สำหรับโจทย์ "ต้นไม้สอง (Two Tree)"
    """
    random.seed(test_case_number)

    # Sample 1
    if test_case_number == 0:
        return "6\n2 5\n3 4\n11 11\n8 9\n18 6\n7 8\n"
    # Sample 2
    elif test_case_number == 1:
        return "2\n9 2\n4 3\n"

    # Subtask 1: N < 50
    elif 2 <= test_case_number <= 5:
        N = random.randint(40, 49)
    # Subtask 2: Full constraints
    else:
        N = random.randint(180, 200)

    tree_data = {}
    nodes_to_process = [1]
    next_node_id = 2

    # Generate a valid tree structure
    while nodes_to_process and next_node_id <= N:
        current_node = nodes_to_process.pop(0)

        # Decide left child
        if next_node_id <= N and random.choice([True, False]):
            left_child = next_node_id
            nodes_to_process.append(left_child)
            next_node_id += 1
        else:
            left_child = random.randint(N + 1, 2 * 10**9)

        # Decide right child
        if next_node_id <= N and random.choice([True, False]):
            right_child = next_node_id
            nodes_to_process.append(right_child)
            next_node_id += 1
        else:
            right_child = random.randint(N + 1, 2 * 10**9)

        tree_data[current_node] = f"{left_child} {right_child}"

    # Handle any remaining nodes as leaves
    remaining_nodes = list(range(1, N + 1))
    for node_id in tree_data:
        if node_id in remaining_nodes:
            remaining_nodes.remove(node_id)

    for node_id in nodes_to_process: # nodes created but not processed
         if node_id in remaining_nodes:
            remaining_nodes.remove(node_id)

    for node_id in remaining_nodes: # nodes never created or processed
        l = random.randint(N + 1, 2 * 10**9)
        r = random.randint(N + 1, 2 * 10**9)
        tree_data[node_id] = f"{l} {r}"


    # Build the final input string
    lines = [str(N)]
    for i in range(1, N + 1):
        lines.append(tree_data.get(i, f"{N+1} {N+2}")) # Failsafe

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
