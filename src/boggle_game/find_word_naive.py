# naive implementation of the boggle game, does not snake around to find matching words
#
# a board is a square matrix, e.g. a 3x3 board
# [["a", "p", "n"],
#  ["p", "i", "u"],
#  ["p", "n", "r"]]
#
# and suppose the following is the targeted words
#  ["app", "boy", "pin", "run", "air", "urn", "pineapple"]
#
# function is expected to return matching words in this implementation
# ["app", "pin", "run", "air"]

def in_board(r, c, size_of_board):
    return 0 <= r < size_of_board and 0 <= c < size_of_board

def match(board, r, c, word):
    # perform scans in 8 different directions
    scan_up, scan_down, scan_left, scan_right = True, True, True, True
    scan_ul, scan_ur, scan_ll, scan_lr = True, True, True, True

    n = len(board)
    # skip checking the first letter
    for i in xrange(1, len(word)):
        ltr = word[i]
        up_row = r - i
        down_row = r + i
        left_col = c - i
        right_col = c + i
        if scan_up:
            scan_up = in_board(up_row, c, n) and board[up_row][c] == ltr
        if scan_down:
            scan_down = in_board(down_row, c, n) and board[down_row][c] == ltr
        if scan_left:
            scan_left = in_board(r, left_col, n) and board[r][left_col] == ltr
        if scan_right:
            scan_right = in_board(r, right_col, n) and board[r][right_col] == ltr
        if scan_ul:
            scan_ul = in_board(up_row, left_col, n) and board[up_row][left_col] == ltr
        if scan_ur:
            scan_ur = in_board(up_row, right_col, n) and board[up_row][right_col] == ltr
        if scan_ll:
            scan_ll = in_board(down_row, left_col, n) and board[down_row][left_col] == ltr
        if scan_lr:
            scan_lr = in_board(down_row, right_col, n) and board[down_row][right_col] == ltr
    return scan_up or scan_down or scan_left or scan_right \
           or scan_ul or scan_ur or scan_ll or scan_lr

def find_words(board, target_words):
    matched_words = set()
    n = len(board)
    for word in target_words:
        for r in xrange(n):
            for c in xrange(n):
                # look for the first matching letter
                if board[r][c] == word[0]:
                    if match(board, r, c, word):
                        matched_words.add(word)
    return matched_words


if __name__ == "__main__":
    board =  [["a", "p", "n"],
              ["p", "i", "u"],
              ["p", "n", "r"]]
    target_words = ["app", "boy", "pin", "run", "air", "urn", "pineapple"]
    print find_words(board, target_words)