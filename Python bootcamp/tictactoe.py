
def initialize():
        p1 = '1'
        board = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8}
        while p1 != 'X' and p1 != 'O':
                p1 = input("WELCOME PLAYERS! \nPlayer 1, please select X or O: ")
                p1 = p1.upper()
                # print(p1)
                # print(p1 == 'X')
                # print(p1 == 'O')
                # print(p1 != 'X' and p1 != 'O')
                if p1 != 'X' and p1 != 'O':
                        print("Please enter X or O.")

        if p1 == 'X':
                players = {'player1' : 'X', 'player2' : 'O'}
        else:
                players = {'player1' : 'O', 'player2' : 'X'}

        return players, board

def display_board(board=None,choices=None,choice=None):
        if board == None:
                a,b,c,d,e,f,g,h,i = ' ' * 9
        else:
                #loop indexes of choices
                #use index to look up letter in dictionary
                #assign letter value at index in list
                pass

        print("  {}  |  {}  |  {}  ".format(a,b,c))
        print("-----------------")
        print("  {}  |  {}  |  {}  ".format(d,e,f))
        print("-----------------")
        print("  {}  |  {}  |  {}  ".format(g,h,i))

def user_selection():
        pass

def tic_tac_toe(players,board):
        pass
        #ask user to select position (store position in list size 9, each index correlates to position on board) authenticate input
        choice = user_selection()
        #update player selection list and check if someone has won
        choices = [None]
        #display new list and say who won or ask next player

        #After win, ask to play again

def main():
        #game setup (dictionary to remember p1 as x/o and p2 as x/o) dictionary mapping a-i to 0-8
        players, board = initialize()
        #display empty game board (use formating curly braces to easily update board)
        display_board()
        
        #play game
        tic_tac_toe(players,board)

        

if __name__ == "__main__":
        main()