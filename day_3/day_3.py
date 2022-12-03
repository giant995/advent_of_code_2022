from itertools import islice


def main():
    priority_sum = 0
    badge_priority_sum = 0
    with open("input.txt", "r") as infile:
        while True:
            next_three_lines = [i.rstrip() for i in islice(infile, 3)]
            if not next_three_lines:
                break

            lines = []
            # part 1
            for line in next_three_lines:
                first_half = set(line[:len(line)//2])
                second_half = set(line[len(line)//2:])
                same_item = first_half.intersection(second_half)
                letter = next(iter(same_item))
                priority_sum += _get_priority(letter)
                lines.append(set(line))

            # part 2
            badge_item = lines[0].intersection(lines[1], lines[2])
            badge_priority_sum += _get_priority(next(iter(badge_item)))

    print(f"Part 1: priority sum is {priority_sum}")
    print(f"Part 2: badge priority sum is {badge_priority_sum}")


def _get_priority(letter):
    if letter.islower():
        return ord(letter)-96
    else:
        return ord(letter)-38


if __name__ == "__main__":
    main()
