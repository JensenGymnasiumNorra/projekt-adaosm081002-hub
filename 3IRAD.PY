
def create_board():
    return [["_" for _ in range (3)] for _ in range (3)]


def print_board(board):
    print("  1 2 3")
    for index, row in enumerate(board):
         line = " ".join(row) 
         print(f"{chr(ord('A') + index) } {line}")
    print( )
  