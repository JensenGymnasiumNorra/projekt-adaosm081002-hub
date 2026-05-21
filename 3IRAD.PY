
def create_board():
    return [["_" for _ in range(3)] for _ in range(3)]




def print_board(board):
    print("  1 2 3")
    for index, row in enumerate(board):
        line = " ".join(row)
        print(f"{chr(ord('A') + index)} {line}")
    print()




def parse_move(move):
    move = move.strip().upper().replace(" ", "")
    if len(move) == 2 and move[0] in "ABC" and move[1] in "123":
        row = ord(move[0]) - ord('A')
        col = int(move[1]) - 1
        return row, col


    parts = move.split()
    if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
        row = int(parts[0]) - 1
        col = int(parts[1]) - 1
        if 0 <= row < 3 and 0 <= col < 3:
            return row, col


    return None




def is_valid_move(board, position):
    if position is None:
        return False
    row, col = position
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == "_"




def check_winner(board, symbol):
    for row in board:
        if all(cell == symbol for cell in row):
            return True


    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True


    if all(board[i][i] == symbol for i in range(3)):
        return True
    if all(board[i][2 - i] == symbol for i in range(3)):
        return True


    return False




def board_full(board):
    return all(cell != "_" for row in board for cell in row)




def switch_player(current):
    return "O" if current == "X" else "X"




def play_round():
    board = create_board()
    current_player = "X"


    while True:
        print_board(board)
        move_input = input(f"Spelare {current_player}, ange ruta (A1-C3 eller 1 1): ")
        position = parse_move(move_input)


        if not is_valid_move(board, position):
            print("Ogiltigt drag. Försök igen med en ledig ruta inom A1-C3 eller 1 1.")
            continue


        row, col = position
        board[row][col] = current_player


        if check_winner(board, current_player):
            print_board(board)
            print(f"Spelare {current_player} vinner!")
            return current_player


        if board_full(board):
            print_board(board)
            print("Oavgjort! Ingen vann.")
            return None


        current_player = switch_player(current_player)




def main():
    score = {"X": 0, "O": 0, "Tie": 0}


    print("Välkommen till Tre i rad!")
    while True:
        winner = play_round()
        if winner is None:
            score["Tie"] += 1
        else:
            score[winner] += 1


        print(f"Ställning: X {score['X']} - O {score['O']} - Oavgjort {score['Tie']}")
        again = input("Vill du spela en ny omgång? (J/N): ").strip().upper()
        if again != "J":
            print("Tack för att du spelade!")
            break




if __name__ == "__main__":
    main()

    
    
