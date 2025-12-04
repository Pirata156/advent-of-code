# Advent of Code 2025 - Day 4 - Puzzle 1

import sys

def handle_line(first_line: str, second_line: str, third_line: str, width: int) -> int:
    to_remove = 0
    # Check each position in the second line (excluding padding)
    for i in range(1, width - 1):
        if second_line[i] == '@':
            # Check surroundings and count '@'
            surroundings = [
                first_line[i-1], first_line[i], first_line[i+1],
                second_line[i-1], second_line[i+1],
                third_line[i-1], third_line[i], third_line[i+1]
            ]
            count = sum(1 for roll in surroundings if roll == '@')
            if count < 4:
                to_remove += 1
    return to_remove

def padding_line(lenght: int) -> str:
    return '.' * lenght

def pad_line(line: str) -> str:
    return '.' + line + '.'

def main():
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        print("Usage: python3 puzzle01.py <filename>", file=sys.stderr)
        sys.exit(1)
    accum = 0  # Accumulator for results
    is_first_line = True
    padded_width = 0
    try:
        with open(filename, "r", encoding="utf-8") as f:
            # Assuming file inputs are well-formed
            for line in f:
                line = line.strip()
                line_result = 0
                third_line = pad_line(line)
                if is_first_line:
                    # Get the width of the lines with padding and prepare second line for next iteration
                    is_first_line = False
                    padded_width = len(line) + 2
                    second_line = padding_line(padded_width)
                else:
                    # Process the previous set of three lines.
                    line_result = handle_line(first_line, second_line, third_line, padded_width)
                # Shift lines up for the next iteration.
                first_line = second_line
                second_line = third_line
                # Add to the accumulator the result from this cycle
                accum += line_result
            # Process the last line with a padded empty line below
            line_result = handle_line(first_line, second_line, padding_line(padded_width), padded_width)
            accum += line_result
        print(f"Final Result: {accum}")
    except FileNotFoundError:
        print(f"File not found: {filename}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()