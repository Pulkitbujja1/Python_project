the_board = {"top-l":' ',"top-m":' ',"top-r":' ',
             "mid-l":' ',"mid-m":' ',"mid-r":' ',
             "low-l":' ',"low-m":' ',"low-r":' '        
            }

def printboard(board):
    print(board["top-l"] + "|"+ board["top-m"] + "|" + board["top-r"])
    print("-+-+-")
    print(board["mid-l"] + "|"+ board["mid-m"] + "|" + board["mid-r"])
    print("-+-+-")
    print(board["low-l"] + "|"+ board["low-m"] + "|" + board["low-r"])



Turn = "X"
for i in range(9):
    print("turn of ",Turn,"where did you want to add:")
    player = input()
    the_board[player] = Turn
    if Turn == "X":
        Turn = "O"
    else:
        Turn = "X"

printboard(the_board)