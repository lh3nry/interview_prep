# boggle.py
def dfs(board,d_word,r,c,n,d):
    # print('r',r,'c',c,'dict',d_word)
    # remove from dict but hold onto current board char for ease of termination
    curchar = d_word.pop(board[r][c],None)
    if not d_word:      # terminate when dict is empty
        return True     # we have successfully used all chars in word!
        
    result = False  # initialize a boolean
    
    # don't have to check 'up' since our linear search iterated from above
    # left
    if c > 0 and board[r][c-1] in d_word:
        # print('left')
        result = dfs(board,d_word,r,c-1,n,d)
    # right
    if c < d-1 and board[r][c+1] in d_word:
        # print('right')
        result = dfs(board,d_word,r,c+1,n,d)
    # down
    if r < n-1 and board[r+1][c] in d_word:
        # print('down')
        result = dfs(board,d_word,r+1,c,n,d)
    
    if result: return result

    # we checked adjacent chars and could not continue deeper
    # put the char back into the dict
    d_word[curchar] = curchar
    # print(d_word)
    # print('exiting')
    return False

def boggle_search(board,word):
    n = len(board)      # num rows
    d = len(board[0])   # num columns (dimension)
    
    # put all chars into a dict for quick access later
    d_word = dict()
    for c in word:
        d_word[c] = c
        
    # linear search to find candidate entry points
    for row in range(n):
        for col in range(d):
            # print(row,col,board[row][col])
            if board[row][col] in d_word:
                # print('found candidate')
                if dfs(board,d_word,row,col,n,d):
                    return True
                
    # searched entire board and word could not be found
    return False

board = [
    ["A","F","A","J"],
    ["S","I","V","A"],
    ["E","R","O","C"],
    ["C","X","E","K"],
    ["O","D","F","S"],
    ["D","E","E","E"]
]

# testword = "FIRECODE"
# testword = "AXE"
testword = "JACK"

print(boggle_search(board,"FIRECODE"))
print(boggle_search(board,"AXE"))
print(boggle_search(board,"JACK"))