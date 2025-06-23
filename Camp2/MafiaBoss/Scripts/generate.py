import sys
import random
import subprocess
from pathlib import Path

# --- Configuration ---
SOLUTION_CPP_NAME = "MafiaBoss.cpp"

# --- Path Setup ---
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
SOLUTIONS_DIR = PROJECT_ROOT / "Solutions"
TESTCASES_DIR = PROJECT_ROOT / "TestCases"
INPUTS_DIR = TESTCASES_DIR / "Inputs"
OUTPUTS_DIR = TESTCASES_DIR / "Outputs"
SOLUTION_CPP_PATH = SOLUTIONS_DIR / SOLUTION_CPP_NAME
# ตั้งชื่อไฟล์ executable สำหรับโจทย์นี้โดยเฉพาะ
SOLUTION_EXE_PATH = SOLUTIONS_DIR / "mafiaboss_solution"

def generate_sample_case(test_case_number):
    """Generate predefined sample cases from PDF"""
    if test_case_number == 0:
        return "4 6\n1 2\n1 3\n1 4\n2 3\n2 4\n3 4\n"
    elif test_case_number == 1:
        return "8 7\n1 2\n1 4\n2 3\n2 6\n3 4\n4 5\n7 8\n"
    elif test_case_number == 2:
        return "5 5\n1 2\n1 3\n2 3\n3 4\n4 5\n"
    return None

def generate_complete_graph(N):
    """Generate a complete graph with N vertices"""
    edges = set()
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            edges.add(tuple(sorted((i, j))))
    return edges

def generate_cycle_graph(N):
    """Generate a cycle graph with N vertices"""
    edges = set()
    for i in range(1, N):
        edges.add(tuple(sorted((i, i + 1))))
    edges.add(tuple(sorted((N, 1))))
    return edges

def generate_bipartite_graph(N):
    """Generate a bipartite graph with N vertices"""
    edges = set()
    for i in range(1, N + 1):
        # Connect to a random node in the other partition
        # Partition 1: odd, Partition 2: even
        u = i
        v = random.randint(1, N)
        if (u % 2) == (v % 2): # if in same partition, shift v
            v = v + 1 if v < N else v - 1
        edges.add(tuple(sorted((u, v))))
    return edges

def generate_random_graph(N):
    """Generate a random graph with N vertices"""
    edges = set()
    max_edges = N * (N - 1) // 2
    E_to_gen = random.randint(N - 1, min(max_edges, N * 5)) # dense enough
    while len(edges) < E_to_gen:
        u = random.randint(1, N)
        v = random.randint(1, N)
        if u != v:
            edges.add(tuple(sorted((u, v))))
    return edges

def generate_input(test_case_number):
    """
    ฟังก์ชันสำหรับสร้างข้อมูล input สำหรับโจทย์ "MafiaBoss"
    NOTE: The provided solution is very slow (O(N*(N+E))), so we only generate
    test cases for the first subtask where N is small.
    """
    random.seed(test_case_number)

    # Case 0-2: Sample cases from PDF
    sample_case = generate_sample_case(test_case_number)
    if sample_case is not None:
        return sample_case

    # Test cases for Subtask 1 (N <= 100)
    N = random.randint(80, 100)

    if test_case_number == 3: # Complete graph (K_n), requires N colors
        edges = generate_complete_graph(N)
    elif test_case_number == 4: # Cycle graph (C_n), requires 2 or 3 colors
        edges = generate_cycle_graph(N)
    elif test_case_number == 5: # Bipartite graph (requires 2 colors)
        edges = generate_bipartite_graph(N)
    else: # Random graph
        edges = generate_random_graph(N)

    E = len(edges)

    # Build the final input string
    lines = [f"{N} {E}"]
    for u, v in edges:
        lines.append(f"{u} {v}")

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
                    timeout=1.0 # Add a timeout just in case
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
