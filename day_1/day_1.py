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

    print(max(elf_calories))


if __name__ == "__main__":
    main()
