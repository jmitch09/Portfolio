# initialize()
# Welcome players and choose player ID
def initialize():
        """ 
            input: None
            output: dictionaries containing board mappings and player ID
        """

        p1 = '1'
        board = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i'}
        
        p1 = input("\nWELCOME PLAYERS TO TIC TAC TOE! \n\nPlayer 1, please select X or O: ")
        p1 = p1.upper()
        while p1 != 'X' and p1 != 'O':
                if p1 != 'X' and p1 != 'O':
                        p1 = input("\nPlease enter X or O: ").upper()

        if p1 == 'X':
                players = {'player1':'X','player2':'O'}
        else:
                players = {'player1':'O','player2':'X'}

        return players, board


# display_board(board=None,choices=None)
# print out tic tac toe board
def display_board(board=None,choices=None):
        """ 
            input: board dictionary and a list of choices
            output: None
        """

        if choices == None:
                a,b,c,d,e,f,g,h,i = ' ' * 9
        else:
                for j in range(len(choices)):
                        if board[j] == 'a':
                                a = choices[j]
                        elif board[j] == 'b':
                                b = choices[j]
                        elif board[j] == 'c':
                                c = choices[j]
                        elif board[j] == 'd':
                                d = choices[j]
                        elif board[j] == 'e':
                                e = choices[j]
                        elif board[j] == 'f':
                                f = choices[j]
                        elif board[j] == 'g':
                                g = choices[j]
                        elif board[j] == 'h':
                                h = choices[j]
                        elif board[j] == 'i':
                                i = choices[j]

        print("\n\n  {}  |  {}  |  {}  ".format(a,b,c))
        print("-----------------")
        print("  {}  |  {}  |  {}  ".format(d,e,f))
        print("-----------------")
        print("  {}  |  {}  |  {}  ".format(g,h,i))


# user_selection(choices,players,turn)
# recieve choice from user to update board
def user_selection(choices,players,turn):
        """ 
            input: list of choices, player ID dictionary, string turn 
            output: int or char choice, list of choices
        """

        choice = -1
        while choice not in range(9) and choice != 'E': 
                choice = input("\nPlease enter 0-8 or E to end the game: ")
                if choice.isnumeric():
                        choice = int(choice)
                else:
                        choice = choice.upper()
                
        if choice in range(9):
                if choices[choice] == ' ':
                        choices[choice] = players[turn]
                else:
                        print("\nThat spot is already taken. Please pick again.")
                        return user_selection(choices,players,turn)


        return choice, choices


# check_col(i,choices)
# check for column win
def check_col(i,choices):
        """ 
            input: int, list of choices
            output: char or NoneType
        """
        if choices[i] == ' ':
                return None
        
        if choices[i] == choices[i + 3] and choices[i] == choices[i + 6]:
                return choices[i]
        else:
                return None
        

# check_row(i,choices)
# check for row win    
def check_row(i,choices):
        """ 
            input: int, list of choices
            output: char or NoneType
        """
        if choices[i] == ' ':
                return None
        
        if choices[i] == choices[i + 1] and choices[i] == choices[i + 2]:
                return choices[i]
        else:
                return None


# check_win(choices,players)
# inspect tic tac toe board for a win
def check_win(choices,players):
        """ 
            input: list of choices, player ID dictionary
            output: bool win
        """
        win = False
        r = None

        for i in range(3):
                r = check_col(i,choices)
                if r == 'X' or r == 'O':
                        break

        if r == None:
                for i in range(0,len(choices),3):
                        r = check_row(i,choices)
                        if r == 'X' or r == 'O':
                                break

        if r == None:
                if choices[0] == choices[4] and choices[0] == choices[8]:
                        r = choices[0]
                elif choices[2] == choices[4] and choices[2] == choices[6]:
                        r = choices[2]

        if r == 'X' or r == 'O':
                win = True

        if win == True:
                if players['player1'] == r:
                        winner = "Player 1"
                else:
                        winner = "Player 2"

                print("\nCongratulations {}! You win!\n".format(winner))

        return win


# replay()
# ask player to play again
def replay():
        """ 
            input: None
            output: char play2
        """
        play2 = None
        while play2 != 'Y' and play2 != 'N':
                play2 = input("Want to play again? (Y/N): ").upper()
                if play2 != 'Y' and play2 != 'N':
                        print("\nI don't understand... Please answer Y or N.\n")

        return play2


# tic_tac_toe(players,board)
# game controller to manage game gunctionality
def tic_tac_toe(players,board):
        """ 
            input: player ID dictionary, board mapping dictionary
            output: None
        """
        play = True
        win = False
        choices = [' ']*9
        turn = 'player1'
        while play:
                choice, choices = user_selection(choices,players,turn)
                
                if choice == 'E':
                        print("\nThanks for playing. Bye!")
                        return
                
                display_board(board,choices)

                if turn == 'player1':
                        turn = 'player2'
                elif turn == 'player2':
                        turn = 'player1'

                #check who wins, reset if win and wants to play again else escape
                win = check_win(choices,players)

                if win == True:
                        play2 = replay()

                        if play2 == 'Y':
                                win = False
                                choices = [' ']*9
                                turn = 'player1'
                                display_board()
                        else:
                                print("\nThanks for playing. Bye!")
                                return


# main()
def main():
        """ 
            input: None
            output: None
        """
        players, board = initialize()
        
        display_board()
        
        tic_tac_toe(players,board)

        

if __name__ == "__main__":
        main()