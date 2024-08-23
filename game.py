class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choosen_name(self):
        while True:
            name = input("Enter your name: ")
            if name.isalpha():
                self.name = name
                break
            else:
                print("Invalid name, please use letters only.")

    def choosen_symbol(self):
        while True:
            symbol = input(f"{self.name}, enter your symbol: ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            else:
                print("Invalid symbol, please use a single letter.")


class Menue:
    def __init__(self):
        pass

    def display_main_menue(self):
        print("Welcome To Tac Toe Game")
        print("1. Start Game")
        print("2. Quit Game")
        while True:
            choice = int(input("Enter Your Choice (1 or 2): "))
            if choice == 1 or choice == 2:
                return choice
            else:
                print("Invalid choice, please try again.")

    def display_endGame_menue(self):
        print("Game Over")
        print("1. Start Game")
        print("2. Quit Game")
        while True:
            choice = int(input("Enter Your Choice (1 or 2): "))
            if choice == 1 or choice == 2:
                return choice
            else:
                print("Invalid choice, please try again.")


class Board:
    def __init__(self):
        self.board_list = [str(i) for i in range(1, 10)]

    def display_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board_list[i:i+3]))
            if i < 6:
                print("-" * 5)

    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board_list[choice - 1] = symbol
            return True
        else:
            return False

    def is_valid_move(self, choice):
        return self.board_list[choice - 1].isdigit()

    def reset_board(self):
        self.board_list = [str(i) for i in range(1, 10)]


'''
x=["1","2","3","4","5","6","7","8","9"]
for i in range(0,10,3):
    print("|".join(x[i:i+3]))
    if i<10:
      print(("-"*5))
'''

class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menue = Menue()
        self.current_player_index = 0

    def start_game(self):
        choice = self.menue.display_main_menue()
        if choice == 1:
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()

    def setup_players(self):
        for number, player in enumerate(self.players, start=1):
            print(f"Player {number}, enter your details:")
            print("*****************************")
            player.choosen_name()
            player.choosen_symbol()
            print("================================")

    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win():
                winner = self.players[1 - self.current_player_index]
                print(f"{winner.name} wins!")
                break
            elif self.check_draw():
                print("It's a draw!")
                break

        choice = self.menue.display_endGame_menue()
        if choice == 1:
            self.restart_game()
        else:
            self.quit_game()

    def restart_game(self):
        self.board.reset_board()
        self.current_player_index=0
        self.play_game()
    def quit_game(self):
        print("Thank you for playing! Goodbye!")


    def play_turn(self):
        player=self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol})")
        while True:
         try: 
            #make sure that user enter int between 1-9
            cell_choice=int(input("Choose cell (1-9): "))
            if 1<=cell_choice <=9 and self.board.update_board(cell_choice,player.symbol): ##make sure that cell choice is valid to put symbol
                break
            else:
                print("Invalid move, Try again")

         except ValueError:
             print("please enter number between(1-9): ")
        self.switch_player()
       

    def  switch_player(self):
         self.current_player_index= 1-self.current_player_index
        #current= 1-0=1  #identify the turn of each player
        #current=1-1=0

    def check_win(self):
       winning_list=[
           [0,1,2],[3,4,5],[6,7,8], #rows
           [0,3,6],[1,4,7],[2,5,8], #columns
           [0,4,8], [2,4,6]  #diagonals

       ]
       for li in winning_list: #[0,1,2] #[3,4,5] ...
           if(self.board.board_list[li[0]] == self.board.board_list[li[1]] == self.board.board_list[li[2]]):
               return True
           print(f"")
       return False

    def check_draw(self):
       #return true if all cells not digits (x or o)
       return all ( not cell.isdigit() for cell in self.board.board_list )
    



g = Game()
g.start_game()
