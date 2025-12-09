# Advent of Code 2025 - Day 6 - Puzzle 2

import sys

def main():
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        print("Usage: python3 puzzle02.py <filename>", file=sys.stderr)
        sys.exit(1)
    accum = 0        # Accumulator for results
    lines = []       # Stores all data lines (excluding newline)
    operations = ''  # Will contain the last line, which defines the operations
    try:
        with open(filename, "r", encoding="utf-8") as f:
            # Assuming file inputs are well-formed
            # Read every line and strip the trailing newline
            for line in f:
                lines.append(line[:-1])  # Strip newline
        # Last line contains operations so move it.
        operations = lines[-1]
        lines.remove(operations)
        current_operation = ''  # The operation currently in effect
        process_accum = 0       # Accumulator for the "current problem"
        # Iterate horizontally across columns of the input (left → right)
        for i in range(len(operations)):
            concatenated = ''   # Will hold the vertical number constructed from lines[*][i]
            # If this column contains an operation symbol, a new problem begins
            if (operations[i] != ' '):
                current_operation = operations[i]
                # Initialize accumulator using neutral element
                if current_operation == '+':
                    process_accum = 0
                else:  # current_operation == '*'
                    process_accum = 1
            # Build the vertical number by taking the i-th character from each of the numbers lines
            for j in range(len(lines)):
                concatenated += lines[j][i]
            concatenated = concatenated.strip()
            # If concatenated is not empty, convert to int and apply operation
            if concatenated != '':
                num = int(concatenated)
                if current_operation == '+':
                    process_accum += num
                else:  # current_operation == '*'
                    process_accum *= num
            # If every character is empty from all lines means the end of problem
            else:
                accum += process_accum
        # After loop ends, add the final accumulated problem result
        accum += process_accum
        print(f"Final Result: {accum}")
    except FileNotFoundError:
        print(f"File not found: {filename}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()