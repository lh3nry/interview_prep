def find_min(inlist):
    i = 0
    m = inlist[i]
    
    for x in range(1,len(inlist)):
        if inlist[x] < m:
            m = inlist[x]
            i = x
    
    return (i,m)
        

def min_triangle_depth(input_dict):
    print(input_dict)
    n = maxlen = len(input_dict)
    s = 0
    entry = find_min(input_dict[n-1])
    
    for x in range(n-1,0,-1):  # bottom up
        # print(i,x)
        curlen = len(input_dict[x])
        if x == n-1: i, s = entry[0],entry[1]
        next_left = i-1 if i > 0 else -1
        next_right = i if i < curlen - 1 else -1
        # print(next_left,next_right)
        lval = input_dict[x-1][next_left] if next_left >= 0 else float('inf')
        rval = input_dict[x-1][next_right] if next_right >= 0 else float('inf')

        if rval > lval:
            s += lval
            i -= 1
        else:
            s += rval
        print(lval,rval,s,x)
        # print(i,s)
        
    # s += input_dict[0][0]
    
    return s


# triangle = [[1], [1, 0], [1, 2, 3], [7, 2, 3, 1]]

print(min_triangle_depth([[1], [1, 0], [1, 2, 3], [7, 2, 3, 1]]))
print(min_triangle_depth([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]))