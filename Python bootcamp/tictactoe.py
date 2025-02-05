
def initialize():
        p1 = '1'
        board = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i'}
        
        p1 = input("WELCOME PLAYERS! \n\nPlayer 1, please select X or O: ")
        p1 = p1.upper()
        while p1 != 'X' and p1 != 'O':
                # print(p1)
                # print(p1 == 'X')
                # print(p1 == 'O')
                # print(p1 != 'X' and p1 != 'O')
                if p1 != 'X' and p1 != 'O':
                        p1 = input("\nPlease enter X or O: ").upper()

        if p1 == 'X':
                players = {'player1':'X','player2':'O'}
        else:
                players = {'player1':'O','player2':'X'}

        return players, board

def display_board(board=None,choices=None,choice=None):
        if choice == None:
                a,b,c,d,e,f,g,h,i = ' ' * 9
        else:
                #loop indexes of choices
                #use index to look up letter in dictionary
                #assign letter value at index in list
                pass

        print("\n\n  {}  |  {}  |  {}  ".format(a,b,c))
        print("-----------------")
        print("  {}  |  {}  |  {}  ".format(d,e,f))
        print("-----------------")
        print("  {}  |  {}  |  {}  ".format(g,h,i))

def user_selection(choices,turn):
        choice = -1
        while choice not in range(9) and choice != 'E': 
                choice = input("\nPlease enter 0-8 or E to end the game: ")
                if choice.isnumeric():
                        choice = int(choice)
                else:
                        choice = choice.upper()
                # print(choice)
                # print(choice not in range(9))
                # print(choice != 'E')
                # print(choice not in range(9) and choice != 'E')

        #update choices with X or O at the index if choice is 0-8
        #return False if E else True
        if choice == 'E':
                return choice, choices, False


        return choice, choices, True

def tic_tac_toe(players,board):
        play = True
        choices = [' '*9]
        turn = 'player1'
        while play:
                #ask user to select position (store position in list size 9, each index correlates to position on board) authenticate input
                choice, choices, play = user_selection(choices,turn)
                if play == False:
                        return
                #update player selection list and check if someone has won
                #display new list and say who won or ask next player
                display_board()
                if turn == 'player1':
                        turn = 'player2'
                elif turn == 'player2':
                        turn = 'player1'

                #After win, ask to play again if yes clear data else return

def main():
        #game setup (dictionary to remember p1 as x/o and p2 as x/o) dictionary mapping a-i to 0-8
        players, board = initialize()
        #display empty game board (use formating curly braces to easily update board)
        display_board()
        
        #play game
        tic_tac_toe(players,board)

        

if __name__ == "__main__":
        main()