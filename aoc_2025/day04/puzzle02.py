# Advent of Code 2025 - Day 4 - Puzzle 2

import sys

# Process a single line with its surrounding lines and gives the number of removals and the new line state
def handle_line(first_line: str, second_line: str, third_line: str, line_size: int) -> tuple[int, str]:
    removables = 0
    new_line = list(second_line)
    # Check each position in the second line (excluding padding)
    for i in range(1, line_size - 1):
        if second_line[i] == '@':
            # Check surroundings and count '@'
            surroundings = [
                first_line[i-1], first_line[i], first_line[i+1],
                second_line[i-1], second_line[i+1],
                third_line[i-1], third_line[i], third_line[i+1]
            ]
            count = sum(1 for roll in surroundings if roll == '@')
            # If less than 4, mark for removal (with 'X')
            if count < 4:
                removables += 1
                new_line[i] = 'X'
    new_line = ''.join(new_line)
    return removables, new_line

def padding_line(lenght: int) -> str:
    return '.' * lenght

def pad_line(line: str) -> str:
    return '.' + line + '.'

def main():
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        print("Usage: python3 puzzle02.py <filename>", file=sys.stderr)
        sys.exit(1)
    global_accum = 0  # Accumulator for results
    process_accum = -1  # Accumulator for current processing
    grid = []
    first_time = True
    line_size = 0  # Size of lines including padding
    try:
        with open(filename, "r", encoding="utf-8") as f:
            # Assuming file inputs are well-formed
            for line in f:
                # Collect all the lines to a grid
                if first_time:
                    # Set the line size with padd and add top padding line
                    first_time = False
                    line_size = len(line) + 2
                    grid.append(padding_line(line_size))
                grid.append(pad_line(line.strip()))
            grid.append(padding_line(line_size))  # Add bottom padding line
            # Process the grid until no more removals occur
            while process_accum != 0:
                process_accum = 0
                # Store the previous line so we can process it on the next iteration
                unchanged_first_line = grid[0]
                # Process centered on each line except the padding ones
                for i in range(1, len(grid) - 1):
                    res, new_second_line = handle_line(unchanged_first_line, grid[i], grid[i+1], line_size)
                    unchanged_first_line = grid[i]
                    grid[i] = new_second_line  # Update the grid line after processing
                    process_accum += res  # Accumulate removals for this pass
                # Update the global accumulator with this pass's removals
                global_accum += process_accum
        print(f"Final Result: {global_accum}")
    except FileNotFoundError:
        print(f"File not found: {filename}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()