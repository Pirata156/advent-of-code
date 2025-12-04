# Advent of Code 2025 - Day 3 - Puzzle 2

import sys

def handle_line(line: str) -> int:
    # Find the 12 highest digits in the line
    concatenated = ''  # Accumulator for concatenated digits
    cursor = 0  # Current position in the line
    for i in range(12):
        # Search only in the substring from the current position up to the last index
        # where enough digits remain to complete the remaining selections.
        remaining_picks = 11 - i
        end_index = len(line) if remaining_picks == 0 else -remaining_picks
        working_line = line[cursor:end_index]
        highest = max(working_line)
        cursor += working_line.index(highest) + 1
        # Append the found highest digit to the result
        concatenated += highest
    return int(concatenated)


def main():
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        print("Usage: python3 puzzle02.py <filename>", file=sys.stderr)
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