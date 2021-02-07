import copy


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        ans = {}
        if not board:
            return []
        board_height = len(board)
        board_width = len(board[0])
        total_size = board_height * board_width
        # Construct trie for the words to be found
        for word in words:
            # print(len(word), total_size)
            if len(word) > total_size:
                continue
            prev_dict = trie
            for c in (word + '-'):
                if not prev_dict.get(c):
                    prev_dict[c] = {}
                    if c == '-':
                        prev_dict[c] = word
                prev_dict = prev_dict[c]

        # print(trie)

        # Find word in trie
        # prev_dict = trie
        # for c in "oath-":
        #     if type(prev_dict.get(c)) != dict:
        #         break
        #     else:
        #         prev_dict = prev_dict.get(c)
        #         if c == '-':
        #             print('True')
        #             break

        # As we iterate each letter on board, we search in the trie if it matches
        def find_on_board(new_board, remain_trie, curr_xy):
            curr_y, curr_x = curr_xy
            nxt_trie = remain_trie.get(new_board[curr_y][curr_x], False)
            if type(nxt_trie) == dict:  # Found a valid path
                # Line up surroundings
                nxt_moves = [(curr_y + 1, curr_x), (curr_y - 1, curr_x), (curr_y, curr_x + 1), (curr_y, curr_x - 1)]
                nxt_moves = list(
                    filter(lambda x: x[0] >= 0 and x[0] < board_height and x[1] >= 0 and x[1] < board_width, nxt_moves))
                if '-' in nxt_trie:
                    ans[nxt_trie['-']] = True
                # new_board = copy.deepcopy(new_board)
                temp_a = new_board[curr_y][curr_x]
                new_board[curr_y][curr_x] = '0'
                for nxt_move in nxt_moves:
                    find_on_board(new_board, nxt_trie, nxt_move)
                new_board[curr_y][curr_x] = temp_a

        for y in range(len(board)):
            for x in range(len(board[0])):
                if type(trie.get(board[y][x])) == dict:  # Found the first letter
                    find_on_board(board, trie, (y, x))

        return (list(ans))

# Trie, one pass across all board to check for trie at all once, backtracking
# Boardsize: n x m
# Number of words: w
# Maximum length of word: l; l < n*m
# Time: O(n*m*w*l + w*l)
# Space: O(w*l)
# Runtime: 460 ms, faster than 28.81% of Python3 online submissions for Word Search II.
# Memory Usage: 27.1 MB, less than 100.00% of Python3 online submissions for Word Search II.