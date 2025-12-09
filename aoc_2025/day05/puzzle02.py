# Advent of Code 2025 - Day 5 - Puzzle 2

import sys

# List of tuples representing fresh ingredient ranges. List is kept sorted and non-overlapping
fresh_ranges = []

# Add a new range of fresh ingredients, merging with any overlapping ranges
def add_range(start: int, end: int) -> None:
    i = 0
    while i < len(fresh_ranges):
        current_start, current_end = fresh_ranges[i]
        # Case 1: New range begins before the current range
        if start < current_start:
            # 1A: New range ends before the current range → insert before, no overlap
            if end < current_start:
                fresh_ranges.insert(i, (start, end))
                return
            # 1B: New range overlaps partially but ends inside current range
            elif end <= current_end:
                # Expand current range to include new start
                fresh_ranges[i] = (start, current_end)
                return
            # 1C: New range fully covers current range or extends past it
            else:
                # Expand current range to include new start and new end
                fresh_ranges[i] = (start, end)
                # Check if this new expanded range overlaps the next one(s)
                check_next(i)
                return
        # Case 2: New range begins inside or exactly at the current range
        else:
            # 2A: New range overlaps or touches current range
            if start <= current_end:
                # New range is fully contained → nothing to add
                if end <= current_end:
                    return
                # New range extends past current → merge by updating the end
                else:
                    fresh_ranges[i] = (current_start, end)
                    # Merge with any following ranges that overlap
                    check_next(i)
                    return
            # 2B: No overlap → move to next range
            else:
                i += 1
    # If we reach here, new range goes at the end (no overlaps)
    fresh_ranges.append((start, end))

# Check and merge the current range with the next one(s) if they overlap
def check_next(index: int) -> None:
    current_start, current_end = fresh_ranges[index]
    if index + 1 < len(fresh_ranges):
        next_start, next_end = fresh_ranges[index + 1]
        # If the next range overlaps or touches the current one
        if next_start <= current_end + 1:
            # Case 1: The next range is fully inside the current one → remove it
            if next_end <= current_end:
                del fresh_ranges[index + 1]
            # Case 2: The next range extends beyond the current one → merge them
            else:
                fresh_ranges[index] = (current_start, next_end)
                del fresh_ranges[index + 1]
            # Recursively check the next range again
            check_next(index)

def count_fresh_ingredients() -> int:
    count = 0
    for start, end in fresh_ranges:
        count += (end - start + 1)
    return count

def main():
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        print("Usage: python3 puzzle02.py <filename>", file=sys.stderr)
        sys.exit(1)
    accum = 0  # Accumulator for results
    try:
        with open(filename, "r", encoding="utf-8") as f:
            # Assuming file inputs are well-formed
            for line in f:
                line = line.strip()
                if len(line) == 0:
                    break
                parts = line.split('-')
                start = int(parts[0])
                end = int(parts[1])
                add_range(start, end)
        result = count_fresh_ingredients()
        print(f"Final Result: {result}")
    except FileNotFoundError:
        print(f"File not found: {filename}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()