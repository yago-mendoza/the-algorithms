board = ([["o","a","a","n"],
          ["e","t","a","e"],
          ["i","h","k","r"],
          ["i","f","l","v"]])

words = ["oath","pea","eat","rain"]



board = [["a","b"],["c","d"]]
words = ["abcb"]




def a_next_b (board,a,b):
    # "a" admite un caracter string o un conjunto de posiciones [(i,j), ...]
    rs = []
    if isinstance(a,str):
        targets = []
        X,Y = len(board),len(board[0])
        for i in range(X):
            for j in range(Y):
                if a == board[i][j]:
                    targets.append((i,j))
    else:
        targets = a
    for target in targets:
        i, j = target
        for mod1 in (-1,0,1):
            for mod2 in (-1,0,1):
                ii, jj = i+mod1, j+mod2
                if (ii < 0 or ii > X-1) or (jj < 0 or jj > Y-1):
                    pass
                else:
                    if board[ii][jj] == b:
                        rs.append((ii,jj))
    return rs

yes_it_is_words = []

interdits = []
for word in words:
    print(word)
    first,*rest=word # o, [a,t,h]
    rest.reverse() # [h,t,a]
    valid = True
    start_point = first
    while rest != []:
        target = rest.pop()

        next_start_points = a_next_b(board,start_point,target)

        if next_start_points == []:
            valid = False
            break
        else:
            start_point = target
    if valid:
        yes_it_is_words.append(word)
        
print(yes_it_is_words)

