
def main():
    inefficient_ranges_count = 0
    with open("input.txt", "r") as f:
        for line in f:
            first_part, second_part = line.rstrip().split(",")
            first_part = first_part.split("-")
            second_part = second_part.split("-")
            overlap = range(
                max(int(first_part[0]), int(second_part[0])), min(int(first_part[-1]), int(second_part[-1])) + 1
            )
            first_part_range_len = int(first_part[-1])-int(first_part[0])+1
            second_part_range_len = int(second_part[-1])-int(second_part[0])+1
            overlap_len = len(overlap)
            if overlap_len > 0 and (first_part_range_len == overlap_len or second_part_range_len == overlap_len):
                inefficient_ranges_count += 1

    print(f"Part 1: there are {inefficient_ranges_count} inefficient ranges")


def range_subset(range1, range2):
    return all(e in range2 for e in range1) or all(e in range1 for e in range2)


if __name__ == "__main__":
    main()
