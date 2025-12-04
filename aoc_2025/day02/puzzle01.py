# Advent of Code 2025 - Day 2 - Puzzle 1

import sys

def make_full(half: int) -> int:
    half_str = str(half)
    full_str = half_str + half_str
    return int(full_str)

def handle_element(pair: tuple[str, str]) -> int:
    result_accum = 0
    s_min, s_max = pair  # Original strings
    range_min = int(s_min)  # Lower range limit
    range_max = int(s_max)  # Upper range limit
    half_string = s_min[:(len(s_min)//2)]
    if (len(s_min) % 2 == 0):
        # If even length, take half directly.
        current_half = int(half_string)
    else:
        # If odd length, minimum valid half has to be one digit longer
        current_half = int('1' + '0' * (len(half_string)))
    current_number = make_full(current_half)
    # Check if invalid numbers are within range
    while (current_number <= range_max):
        if (current_number >= range_min):
            # Only accumulate if within range
            result_accum += current_number
        # Calculate next invalid number
        current_half += 1
        current_number = make_full(current_half)
    return result_accum

def main():
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        print("Usage: python3 puzzle01.py <filename>", file=sys.stderr)
        sys.exit(1)
    accum = 0  # Accumulator for results
    try:
        with open(filename, "r", encoding="utf-8") as f:
            # Assuming file inputs are well-formed
            line = f.read().strip()
            list_pairs = [tuple(element.split('-')) for element in line.split(',')]
            for pair in list_pairs:
                result = handle_element(pair)
                # Increase accum with result from each pair
                accum += result
        print(f"Final Result: {accum}")
    except FileNotFoundError:
        print(f"File not found: {filename}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()