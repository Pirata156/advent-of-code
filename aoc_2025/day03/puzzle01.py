# Advent of Code 2025 - Day 3 - Puzzle 1

import sys

def handle_line(line: str) -> int:
    # Find the two highest digits in the line in order
    first_highest = max(line[:-1])
    first_position = line.index(first_highest)
    second_highest = max(line[first_position+1:])
    # Return their integer concatenation
    return int(first_highest + second_highest)

def main():
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        print("Usage: python3 puzzle01.py <filename>", file=sys.stderr)
        sys.exit(1)
    accum = 0  # Accumulator for results
    try:
        with open(filename, "r", encoding="utf-8") as f:
            # Assuming file inputs are well-formed.
            for line in f:
                line = line.strip()
                res = handle_line(line)
                accum += res
        print(f"Final Result: {accum}")
    except FileNotFoundError:
        print(f"File not found: {filename}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()