

def main():
    # part 1
    char_counter = get_marker_count(4)
    print(f"Part 1: the first marker came after receiving {char_counter} characters")

    # part 2
    char_counter = get_marker_count(14)
    print(f"Part 2: the second marker came after receiving {char_counter} characters")


def get_marker_count(marker_length):
    char_counter = 0
    with open('input.txt') as f:
        buffer = []
        while True:
            buffer.append(f.read(1))
            char_counter += 1
            if len(buffer) == marker_length:
                if len(set(buffer)) == len(buffer):
                    break
                buffer.pop(0)
    return char_counter


if __name__ == "__main__":
    main()
