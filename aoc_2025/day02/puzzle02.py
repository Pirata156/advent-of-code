# Advent of Code 2025 - Day 2 - Puzzle 2

import sys

# Returns True if value is composed of k >= 2 repetitions of a smaller substring
def is_invalid(value: str) -> bool:
    concat_str = (value + value)[1:-1]
    return value in concat_str

def handle_element(pair: tuple[str, str]) -> int:
    accums = 0  # Accumulator for this pair
    s_min, s_max = pair  # Original strings
    # Check each number in range for invalidity
    for val in range(int(s_min), int(s_max) + 1):
        if is_invalid(str(val)):
            accums += val
    return accums

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
            line = f.read().strip()
            list_pairs = [tuple(element.split('-')) for element in line.split(',')]
            for pair in list_pairs:
                result = handle_element(pair)
                accum += result
        print(f"Final Result: {accum}")
    except FileNotFoundError:
        print(f"File not found: {filename}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()