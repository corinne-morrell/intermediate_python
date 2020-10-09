

def build_board():
    ''' Returns a nested list that contains the names of the squares on a chessboard. Each element of the outer list '''

    chessboard = []

    for number in range(8, 0, -1):
        chessboard.append([])
        for letter in "abcdefgh":
            chessboard[-1].append(letter+str(number))

    return chessboard

def print_board(board):

    for i in range(len(board)):
        print(board[i])

def main():
    board = build_board()
    print_board(board)

if __name__ == "__main__":
    main()