import random as rm

up = True
down = False


class Board:
    def __init__(self, dimension):
        """Class konstruktör som tilldelar ord, bord, poäng och status för korten (upp/ner)."""
        self.dimension = dimension
        self.board = [[0 for x in range(dimension)] for y in range(dimension)]
        self.FaceUpDown = [[down for i in range(len(self.board[x]))] for x in range(len(self.board))]
        self.high_score = 0
        self.get_words()

    def draw_board(self):
        """Metod som kommer rita ut bordet för spelet (siffror, bokstäver, korttillstånd)."""
        for i in range(1, len(self.board) + 1):
            print("   ", i, end="")

        for x in range(len(self.FaceUpDown)):
            print()
            for y in range(len(self.FaceUpDown[x])):
                if y == 0:
                    print(chr(65 + x), end=". ")
                if self.FaceUpDown[x][y] == down:
                    print("---", end="  ")
                elif self.FaceUpDown[x][y] == up:
                    print(self.board[x][y], end="   ")

    def get_words(self):
        """Metod som tar ord från fil och sorterar ut dem i bord spelet."""
        file = open("memo.txt", "r")
        file_words = []
        randomwords = []

        for i, line in enumerate(file):
            file_words.insert(i, line.strip())

        total_card = self.dimension * self.dimension

        if total_card % 2 == 1:
            total_card -= 1
            self.board[self.dimension - 1].pop(self.dimension - 1)
            self.FaceUpDown[self.dimension - 1].pop(self.dimension - 1)

        for i in range(int(total_card / 2)):
            word = file_words[rm.randrange(0, len(file_words))]
            randomwords.insert(i, word)
            randomwords.insert(-i, word)
            rm.shuffle(randomwords)
        rm.shuffle(randomwords)

        wordcount = 0
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                self.board[x][y] = randomwords[wordcount]
                wordcount += 1
        file.close()

    def choice(self):
        """Metod som frågar användaren vilket kort ska vändas och se om kortet matchar."""
        number = 0

        while True:
            choice1 = input("\nChoose the first card to flip: ").strip().upper()
            if len(choice1) == 2:
                char = ''.join(x for x in choice1 if x.isalpha())
                if len(char) == 1:
                    char = ord(char) - 65
                    if 0 <= char < len(self.FaceUpDown):
                        number = int(''.join(x for x in choice1 if x.isdigit()))
                        number -= 1
                        if 0 <= number < len(self.FaceUpDown[char]):
                            if self.face_direction(char, number) == down:
                                self.FaceUpDown[char][number] = up
                                self.draw_board()
                                break
                            else:
                                self.draw_board()
                                print("card already turned try again!: ")
                                continue

            self.draw_board()
            print("\nIncorrect input, try again. ")
            continue

        while True:
            choice2 = input("\nChoose the second card to match: ").strip().upper()
            if len(choice2) == 2:
                char2 = ''.join(x for x in choice2 if x.isalpha())
                if len(char2) == 1:
                    char2 = ord(char2) - 65
                    if 0 <= char2 < len(self.FaceUpDown):
                        number2 = int(''.join(x for x in choice2 if x.isdigit()))
                        number2 -= 1
                        if 0 <= number2 < len(self.FaceUpDown[char2]):
                            if self.face_direction(char2, number2) == down:
                                self.FaceUpDown[char2][number2] = up
                                self.draw_board()
                                break
                            else:
                                self.draw_board()
                                print("\nCard already turned try again!: ")
                                continue

            self.draw_board()
            print("\nIncorrect input try again. ")
            continue

        if self.get_element(char2, number2) != self.get_element(char, number):
            self.FaceUpDown[char][number] = down
            self.FaceUpDown[char2][number2] = down
        else:
            print("\nYou got a match!!")


    def get_element(self, x, y):
        """Metod som överser orden i viss tillåten position."""
        return self.board[x][y]

    def face_direction(self, x, y):
        """Metod som visar om ordet är vänd/ej vänt i tillåten position."""
        return self.FaceUpDown[x][y]

    def play_game(self, player_name):
        """Metod som ritar bordet, hanterar input från användare, lägger in poäng i lista & skriver ut."""
        self.draw_board()
        while not(self.game_over()):
            self.choice()
            self.high_score += 1
        hs_file = open("high_score.txt", "a")
        hs_text = "SCORE: " + str(self.high_score) + " User: " + player_name + " SIZE: " \
                  + str(self.dimension) + "x" + str(self.dimension) + "\n"
        hs_file.write(hs_text)
        hs_file.close()
        self.get_high_score()

    def get_high_score(self):
        """Metod som skriver ut och sorterar poäng med tillagd spelare."""
        hs_list = []
        file = open("high_score.txt", "r")
        for score, line in enumerate(file):
            hs_list.insert(score, line)

        hs_list.sort()
        for players in range(len(hs_list)):
            print(players+1, ".", hs_list[players].strip())

    def game_over(self):
        """Metod som styr om alla ord har hittat sin matchning. """
        for y in range(len(self.FaceUpDown)):
            for x in range(len(self.FaceUpDown[y])):
                if self.FaceUpDown[x][y] == down:
                    return False

        print("You Won!!! Congrats!!!!")
        print("It took you ", self.high_score, " tries to win the game.")
        return True
