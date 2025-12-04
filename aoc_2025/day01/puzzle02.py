# Advent of Code 2025 - Day 1 - Puzzle 2

import sys

def handle_line(dial: int, rotation:str, distance: int):
    clicks = distance // 100  # Full rotations count as clicks
    rest_distance = distance % 100  # Remaining distance after full rotations
    jump = dial
    if rotation == 'L':
        if dial > rest_distance:
            # Going left without crossing the boundary (0)
            jump -= rest_distance
        else:
            # Crosses ore reaches the boundary (0): wrap around from 0 to 100
            jump += (100 - rest_distance)
            # Count extra click only if the boundary cross didn't start or end at the boundary (0)
            if (dial != 0 and jump != 100):
                clicks += 1
    elif rotation == 'R':
        # Going right, add the rest of the distance directly, normalize later
        jump += rest_distance
    # Normalize the overflow from remainder distance
    clicks += jump // 100
    jump = jump % 100
    return jump, clicks

def main():
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        print("Usage: python3 puzzle02.py <filename>", file=sys.stderr)
        sys.exit(1)
    dial = 50  # Dial starting position
    accum = 0  # Accumulator for clicks
    try:
        with open(filename, "r", encoding="utf-8") as f:
            # Assuming file inputs are well-formed.
            for line in f:
                rotation = line[0]
                distance = int(line[1:].strip())
                dial, clicks = handle_line(dial, rotation, distance)
                # Increase accum by number of clicks from this line
                accum += clicks
        
        print(f"Result: {accum}")
    except FileNotFoundError:
        print(f"File not found: {filename}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()