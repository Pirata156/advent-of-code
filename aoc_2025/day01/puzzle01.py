# Advent of Code 2025 - Day 1 - Puzzle 1

import sys

def handle_line(dial: int, rotation:str, distance: int):
    if rotation == 'L':
        # Going left, we subtract and normalize
        dial = (dial - distance) % 100
    elif rotation == 'R':
        # Going right, we add and normalize
        dial = (dial + distance) % 100
    return dial

def main():
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        print("Usage: python3 puzzle01.py <filename>", file=sys.stderr)
        sys.exit(1)
    dial = 50  # Dial starting position
    accum = 0  # Accumulator for dials landing on 0
    try:
        with open(filename, "r", encoding="utf-8") as f:
            # Assuming file inputs are well-formed.
            for line in f:
                rotation = line[0]
                distance = int(line[1:].strip())
                dial = handle_line(dial, rotation, distance)
                # Increase accum if dial landed on 0
                if dial == 0:
                    accum += 1
        
        print(f"Result: {accum}")
    except FileNotFoundError:
        print(f"File not found: {filename}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()