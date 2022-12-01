# declare main
def main():
    elf_calories = []
    with open('input.txt', 'r') as f:
        accumulator = 0
        for line in f:
            if line == '\n':
                elf_calories.append(accumulator)
                accumulator = 0
                continue
            accumulator += int(line)

    print(f"Part 1: the elf with most snacks carries {max(elf_calories)} calories")
    print(f"Part 2: the top three elves with most snacks carry {sum(sorted(elf_calories, reverse=True)[:3])} calories")


if __name__ == "__main__":
    main()
