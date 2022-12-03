def main():
    opponent_hand = ["A", "B", "C"]
    my_hand = ["X", "Y", "Z"]

    my_score = 0
    real_score = 0
    with open("input.txt", "r") as f:
        for line in f:
            moves = line.rstrip().split(" ")
            opponent_move_index = opponent_hand.index(moves[0])
            my_move_index = my_hand.index(moves[1])
            winning_move_pos = my_hand.index(my_hand[(my_move_index+2) % 3])
            my_score += my_move_index + 1
            if my_move_index == opponent_move_index:
                my_score += 3
            elif winning_move_pos == opponent_move_index:
                my_score += 6

            if moves[1] == "X":
                real_score += opponent_hand.index(opponent_hand[(opponent_move_index+2) % 3])+1
            elif moves[1] == "Y":
                real_score += 3
                real_score += opponent_move_index + 1
            elif moves[1] == "Z":
                real_score += 6
                real_score += opponent_hand.index(opponent_hand[(opponent_move_index+1) % 3])+1

    print(f"Part 1: my score is {my_score}")
    print(f"Part 2: real score is {real_score}")


if __name__ == "__main__":
    main()
