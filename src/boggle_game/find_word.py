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

def find_words_naive(board, target_words):
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

def match_word(word_to_match, target_words):
    for word in target_words:
        if word_to_match == word:
            return True
    return False

def _find_words(board, row, col, target_words, matched_words, word, visited):
    visited[row][col] = True  # mark the cell as visited
    word += board[row][col]
    n = len(board)
    if match_word(word, target_words):
        matched_words.add(word)

    # DFS on the adjacent cells
    # be careful with the indexing here, want to traverse neighboring next_row (either up or down) within the boundary [0, n), and [row-1, row+2)
    # same treatment is needed for next_col
    for next_row in xrange(row-1, row+2, 1):
        if 0 <= next_row < n:
            for next_col in xrange(col-1, col+2, 1):
                if 0 <= next_col < n and not visited[next_row][next_col]:
                    _find_words(board, next_row, next_col, target_words, matched_words, word, visited)
    visited[row][col] = False  # reset the visited cell

def find_words(board, target_words):
    """
        return a set of words match any word in the target words
    :param board:
    :param target_words:
    :return:
    """
    matched_words = set()
    n = len(board)
    word = ''  # empty string to construct word
    # visited = [n * [False]] * n # this initialization actually has a funny bug
    visited = [[False] * n for _ in xrange(n)]  # tracker for each cell visited
    for row in xrange(0, n, 1):
        for col in xrange(0, n, 1):
            _find_words(board, row, col, target_words, matched_words, word, visited)
    return matched_words

if __name__ == "__main__":
    board =  [["a", "p", "n"],
              ["p", "i", "u"],
              ["p", "n", "r"]]
    target_words = ["app", "boy", "pin", "run", "air", "urn", "pineapple"]

    print "-------Naive implementation, urn should be omitted---------"
    print find_words_naive(board, target_words)
    print "-------Efficient implementation---------"
    print find_words(board, target_words)

    print "------Let's try a more interesting board to find the pineapple-----"
    new_board =  [["a", "p", "p"],
                  ["e", "p", "l"],
                  ["n", "i", "e"]]
    print find_words(new_board, target_words)