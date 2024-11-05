import board


def main():
    """Main funktion som frågar användare för dimension och börjar spelet."""
    print("Hey and welcome to memory game. Today we are going to test your memory skills: ")
    player_name = input("But first what is your name player: ")
    print("Hey", player_name, "Lets start playing. Do not forgot to do your best to be in the leaderboard!\n")

    dimension = 0
    while dimension < 2 or dimension > 8:
        try:
            dimension = int(input("Enter dimension of the game (between 2 and 8): "))
        except ValueError:
            print("Please enter a valid integer! ")

    game_board = board.Board(dimension)
    game_board.play_game(player_name)


main()
