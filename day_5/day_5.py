import copy


def main():
    dock = []
    instructions = []

    with open("input.txt") as f:
        for line in f:
            spaces = [line[i:i+4].rstrip().replace(" ", "") for i in range(0, len(line), 4)]
            if len(dock) == 0:
                dock = [[] for _ in range(len(spaces))]
            # if we get to the column line, skip 2 lines and break to instructions
            if spaces[0].isdigit():
                next(f)
                break
            for i, space in enumerate(spaces):
                if space:
                    dock[i].append(space)
            pass

        for line in f:
            instructions.append([int(num) for num in line.split() if num.isdigit()])

    # get a copy of the dock
    real_dock = copy.deepcopy(dock)

    for instruction in instructions:
        for _ in range(instruction[0]):
            origin_stack = dock[instruction[1]-1]
            destination_stack = dock[instruction[2]-1]
            destination_stack.insert(0, origin_stack.pop(0))
        # CrateMover 9001 move
        crane_load = [real_dock[instruction[1]-1].pop(0) for _ in range(instruction[0])]
        # revert crane_load
        crane_load.reverse()
        for crate in crane_load:
            real_dock[instruction[2]-1].insert(0, crate)

    top_crates = [stack[0].replace("[", "").replace("]", "") for stack in dock if stack[0]]
    print(f"Part 1: the top crates are {''.join(top_crates)}")

    top_crates = [stack[0].replace("[", "").replace("]", "") for stack in real_dock if stack[0]]
    print(f"Part 2: the top crates are {''.join(top_crates)}")


if __name__ == "__main__":
    main()
