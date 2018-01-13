import copy

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

def msort_ind(L,l,r):
    if r-l < 2:
        print("hit base",l,r)
        merge_ind()
        return
    # n = len(L)
    mid = l+(r-l)//2
    print(l,mid,r)
    msort_ind(L,l,mid)   # left split
    msort_ind(L,mid+1,r)   # right split

def countSort(L,lo,hi,L2):
    if lo >= hi: return 0

    mid = lo+(hi-lo)//2

    count = 0
    count += countSort(L2,lo,mid,L)
    count += countSort(L2,mid+1,hi,L)
    count += countMerge(L,lo,mid,hi,L2)

    # print(lo,mid,hi,count,L[lo:hi])#,L2[lo:hi])
    return count

def countMerge(L,lo,mid,hi,L2):
    count = 0
    i,j,k = lo, mid + 1, lo
    while i<=mid or j<=hi:
        if i > mid:
            # print("i > mid:",i,k,j,L[lo:hi],L2[lo:hi])
            L[k] = L2[j]
            k+=1
            j+=1
        elif j > hi:
            # print("j > hi:",i,k,j,L[lo:hi],L2[lo:hi])
            L[k] = L2[i]
            k+=1
            i+=1
        elif L2[i] <= L2[j]:
            # print("[i] <= [j]:",i,k,j,L[lo:hi],L2[lo:hi])
            L[k] = L2[i]
            k+=1
            i+=1
        else:
            # print("[i] > [j]:",i,k,j,L[lo:hi],L2[lo:hi])
            L[k] = L2[j]
            k+=1
            j+=1
            count += mid + 1 - i
    return count


# a = [1,3,9,2,3,4,6]
a = [2, 1, 3, 1, 2]
b = [-8,-2,-1,-9,-2,-4]

# print(merge(a,b))
# print(msort(a))
# print(msort(b))


# msort_ind(a,0,len(a)-1)
arr = copy.deepcopy(a)
aux = copy.deepcopy(a)
print(countSort(arr,0,len(arr)-1,aux))
print(a)
print(arr,aux)





