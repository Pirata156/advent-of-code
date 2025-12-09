# Advent of Code 2025 - Day 6 - Puzzle 1

import sys

def main():
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        print("Usage: python3 puzzle01.py <filename>", file=sys.stderr)
        sys.exit(1)
    accums = []  # Column accumulators
    operations = ''  # Operations in order of columns
    try:
        # Gets the operations from the last line
        with open(filename, "rb") as f:
            f.seek(-1, 2)  # Goes to before last byte (skips the last '\n')
            end = f.tell()
            pos = end - 1
            # Move backward until we find the beginning of the last line
            while pos >= 0:
                f.seek(pos)
                if f.read(1) == b'\n':
                    break
                pos -= 1
            f.seek(pos + 1)
            last_line = f.read(end - pos - 1).decode().strip()
            operations = last_line.replace(' ', '')
            # Initialize accumulators based on the operations
            accums = [0 if op == '+' else 1 for op in operations]
        # Process the lines in order, except the last one
        with open(filename, "r", encoding="utf-8") as f:
            # Assuming file inputs are well-formed
            for line in f:
                line = line.strip()
                # Skip last line
                if (line == last_line):
                    break
                parts = line.split()  # Get a list of inputs of that line
                for i, op in enumerate(operations):
                    if op == '+':
                        accums[i] += int(parts[i])
                    elif op == '*':
                        accums[i] *= int(parts[i])
        result = sum(accums)
        print(f"Final Result: {result}")
    except FileNotFoundError:
        print(f"File not found: {filename}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()