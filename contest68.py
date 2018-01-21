# contest68.py
def reorganizeString(S):
    """
    :type S: str
    :rtype: str
    """
    if len(S) < 3: return S
    
    hist = {}
    for c in S:
        if c in hist:
            hist[c] += 1
        else: hist[c] = 1
            
    hist_s = list(hist.items())
    hist_s.sort(key = lambda x: (-x[1],x[0]))
    # print(hist_s,[i for _,i in hist_s[1:]])
    if hist_s[0][1] - 1 > sum([i for _,i in hist_s[1:]]) : return ""

    new = [hist_s[0][0]] * hist_s[0][1]
    hist_s.pop(0)
    # print(hist_s)
    pos,pos_pre,ind = 1,1,0

    while hist_s:
        # ind=(ind+1)%len(hist_s)
        # print(len(hist_s),ind)
        char,count = hist_s[ind][0],hist_s[ind][1]
        for i in range(count):
            new = new[:pos] + [char] + new[pos:]
            pos+=2
        hist_s.remove((char,count))
        print("".join(new),hist_s)
        pos = pos_pre + 2*count
        pos_pre = pos
        # print(new,hist_s)
    return "".join(new)




# print(reorganizeString('aaabbccc'))
print(reorganizeString("todrnphcamnomskfrhe"))