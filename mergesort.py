# mergesort.py
def merge(l,r):
    nl = len(l)
    nr = len(r)
    if nl < 1: return r
    if nr < 1: return l
    retlist = []

    while l or r:
        print('left',l,'right',r,'ret',retlist)
        if not l: 
            retlist.extend(r)
            break
        if not r: 
            retlist.extend(l)
            break
            
        if l[0] > r[0]:
            retlist.append(r.pop(0))
        else:
            retlist.append(l.pop(0))
    return retlist
    print('ret',retlist)
    return retlist

def msort(L):
    n = len(L)
    if n < 2: return L
    left = msort(L[:n//2])
    right = msort(L[n//2:])
    return merge(left,right)


a = [1,3,9,2,3,4,6]
b = [-8,-2,-1,-9,-2,-4]

# print(merge(a,b))
print(msort(a))
# print(msort(b))