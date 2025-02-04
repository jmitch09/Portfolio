
def display_board(choices=None, choice=None):
        if choices == None:
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

def main():
        #game setup (dictionary to remember p1 as x/o and p2 as x/o) dictionary mapping a-i to 0-8
        #display empty game board (use formating curly braces to easily update board)
        display_board()
        #ask user to select position (store position in list size 9, each index correlates to position on board) authenticate input
        #update player selection list and check if someone has won
        #display new list and say who won or ask next player

        #After win, ask to play again

if __name__ == "__main__":
        main()