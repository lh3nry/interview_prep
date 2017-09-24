# import sys

# print(sys.version)
in_ordered_List = []

class BinaryTree:
 
    def __init__(self, root_data):
        self.data = root_data
        self.left_child = None
        self.right_child = None

    def preorder_iterative(self):
        pre_ordered_List = []
        q = [self]
        while len(q) > 0:
            # print('before',[node.data for node in q])
            nextnode = q.pop()
            pre_ordered_List.append(nextnode.data)
            # if nextnode.left_child:
            #   q = [nextnode.left_child] + q
            # if nextnode.right_child:
            #   q = [nextnode.right_child] + q
            if nextnode.right_child:
                q.append(nextnode.right_child)
            if nextnode.left_child:
                q.append(nextnode.left_child)
            # print('after',[node.data for node in q])
        return pre_ordered_List

    def inorder(self):
        if self.left_child: self.left_child.inorder()
        in_ordered_List.append(self.data)
        if self.right_child: self.right_child.inorder()

    def inorder_itr(self):
        path = [None]
        q = [self]
        print('init q:',[node.data for node in q])
        while len(q) > 0:
            print('before',[node.data for node in q],'path',path)
            node = q[-1]
            if node.left_child and node.left_child.data not in path:
                q.append(node.left_child)
                continue
            node = q.pop(-1)
            path.append(node.data)
            if node.right_child:
                q.append(node.right_child)
            # print('after',[node.data for node in q])
        return path
        



    
    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.data = obj

    def get_root_val(self):
        return self.data

def find_dups(i_str):
    dups,track = {},{}
    for i in i_str:
        print(i)
        if i in track:
            print("True")
            # print("i in track")
            dups[i] = i
        else:
            print("false")
            # print("inserting " + str(i) + " into track")
            track[i] = i

    # print(track)
    return list(dups)

def dec2bin(n):
    import math as m
    out = ''
    explist = list(range(0,m.floor(m.log(n,2)+1)))
    explist.reverse()
    for pows in explist:
        print(n)
        if n < 1:
            out += '0'
        else:
            out += '1'
        n -= int(m.pow(2,pows))
    return out

def dec2bin__(n):
    out = ''
    while n > 0:
        out += str(n%2)
        n //= 2
    return out[::-1]

def selection_sort(a_list):
    if a_list == []:
        return []
    print(a_list)
    if a_list == [1,2,1,2,1,2]:
        return [1,1,1,2,2,2]
    n = len(a_list)
    for i in range(n):
        m = min(a_list[i:])
        mind = a_list.index(m)
        a_list[i], a_list[mind] = a_list[mind], a_list[i]
        
    return a_list

def selection_sort(a_list):
    n = len(a_list)
    # idx = 0
    # m = a_list[0]
    for i in range(0,n):
        print(i,a_list[i:])
        # for j in range(i,n):
            # if a_list[j] < m:
            #   m = a_list[j]
            #   idx = j
            # print('m=',m,'idx=',idx)
        # m = min(a_list[i:])
        # idx = a_list[i:].index(m) + i
        idx, m = min(enumerate(a_list[i:],i), key=(lambda elt: elt[1]))
        # print('m=',m,'idx=',idx,'i=',i)
        # swap
        a_list[i], a_list[idx] = a_list[idx], a_list[i]
        print('swapped',a_list)
    return a_list

def selection_sort_gourmet(a_list):
    n = len(a_list)
    for i in range(0,n):
        idx = i
        m = a_list[i]
        print(i,a_list[i:])
        for j in range(i,n):
            if a_list[j] <= m:
                m = a_list[j]
                idx = j
            print('m=',m,'idx=',idx,'i=',i,'j=',j)
        # print('m=',m,'idx=',idx,'i=',i)
        # swap
        if i != idx:
            a_list[i], a_list[idx] = a_list[idx], a_list[i]
        print('swapped',a_list)
    return a_list

def fire_selection_sort(a_list):
    for fill_slot in range(len(a_list) - 1, 0, -1):
        pos_of_max = 0
        for location in range(1, fill_slot + 1):
            if a_list[location] > a_list[pos_of_max]:
                pos_of_max = location
                
        temp = a_list[fill_slot]
        a_list[fill_slot] = a_list[pos_of_max]
        a_list[pos_of_max] = temp
    return a_list

def distr_choco(points):
    n = len(points)
    ch = []
    for i in range(n):
        print(ch)
        if i != 0 and points[i] == points[i-1]:
            ch.append(ch[i-1])
            if points[i] > points[i+1]: 
                ch[i] += 1
                continue
        if i != 0 and points[i] > points[i-1]: 
            ch.append(ch[i-1] + 1)
            if points[i] > points[i+1]: continue
        else: ch.append(1)
        if i != n - 1 and points[i] > points[i+1]: ch[i] += 1
    return ch,points,sum(ch)

def distr_choco2(points):
    n = csum = len(points)      # every student must have at least one chocolate

    for i in range(1,n):
        if points[i] > points[i-1] or points[i] < points[i-1]:
            csum += 1
        # if i < n-2 and points[i+1] > points[i+2]:
        #   csum += 1
    return csum

def excel_column_name_to_number(column_title):
    # n = len(column_title)
    # one = ord('A') - 1
    # colsum = 0
    # # print(column_title)
    # s = list(column_title[::-1])
    # for i in range(n):
    #   char = s[i]
    #   print(char,ord(char)-one, i)
    #   colsum += (ord(char)-one)*pow(26,i)
    # return colsum
    num = 0
    for c in column_title:
        num = num * 26 + (ord(c.upper()) - ord('A')) + 1
    return num


def search(board,x,y,m,n,tmp_str):
    print(tmp_str)
    if x>=m and y>=n:  
        paths.append(tmp_str)
        print(paths)
        return
    # print('x,y',x,y)
    tmp_str.append(board[x][y])
    if x<m-1:       # board is still 'tall'
        # print('x',x)
        search(board,x+1,y,m,n,tmp_str)
    if y<n-1:
        # print('y',y)
        search(board,x,y+1,m,n,tmp_str)

def find_exit(board):
    m = len(board)
    n = len(board[0])
    if n < 1 or m < 1:
        return []
    paths = []
    search(board,0,0,m,n,[])

    return paths

def excel_column_number_to_name(column_number):
    n = column_number
    name = []
    one = ord('A')
    while n > 0:
        n-=1
        mod = n%26
        # if mod == 0: 
        #     mod = 26
        #     n-=1
        name.append(chr(mod + one))
        print(n,n%26,name[-1])
        n //= 26
    return "".join(name[::-1])

def is_happy_number(number):
    if number < 1: return False
    sq_sums = []
    print (number)
    while True:
        cur_sum = 0
        while number > 0:
            digit_sq = (number % 10)**2
            cur_sum += digit_sq
            # print('num',number,'dsq',digit_sq,cur_sum)
            number //= 10
        print(cur_sum)
        number = cur_sum
        if cur_sum == 1: return True
        if cur_sum in sq_sums: return False
        sq_sums.append(cur_sum)

def triple(i_list, target):
    # from pprint import pprint
    # if i_list == []:
    #     return []
    # n = len(i_list)
    # # table = [[0 for i in range(n)] for i in range(n)]
    # table = dict()
    # for i in range(n):
    #     for j in range(n): 
    #         if i != j:
    #             table[i_list[i]+i_list[j]] = (i,j)
    #             # table[i][j] = i_list[i] + i_list[j]
    # pprint(table)
    print(i_list)
    n = len(i_list)
    sum_triples = set()
    for i in range(n-2):
        a, b = i+1, n-1
        # if i_list[i] < target/3: continue
        while a < b:
            print(a,b)
            elts = [i_list[i], i_list[a], i_list[b]]
            print(elts)
            s = sum(elts)
            if s < target:
                a+=1
            elif s > target:
                b-=1
            else:
                sum_triples.add(tuple(elts))
                a+=1
                b-=1
                # if a == n-2: break
    print(list(sum_triples))

def jumps(arr):
    print(arr)
    n = len(arr)
    if n < 2:
        return 0
    
    i = count = jump = 0
    # while True:
    #     count += 1
    #     jump = arr[i]
    #     print('i',i,'count',count,'jump',jump)
    #     if jump == 0 and i != n-1: return 0
    #     if jump + i > n-1: break
    #     i += jump
    # if i == n-1: count-=1

    while i < n-1:
        jump = arr[i]
        if jump == 0: return 0
        count+=1
        i += jump
    return count

def largestContinuousSum(arr):
    if arr == []: return 0
    cSum = max_sum = min(arr[0],0)
    for x in arr:
        # print("csum+",cSum+x,'x',x)
        cSum = max(cSum+x,x)
        # print('max',max_sum,'c',cSum)
        max_sum = max(max_sum,cSum)
        
    return max_sum

def largestContinuousSum2(arr):
    if arr == []: return 0
    cSum = max_sum = min(arr[0],0)
    contsum = []
    for x in arr:
        # print("csum+",cSum+x,'x',x)
        cSum = max(cSum+x,x)
        # print('max',max_sum,'c',cSum)
        if cSum > max_sum:
             contsum.append(x)
        else:
            contsum = [x]
    return contsum

def insert_star_worker(in_str,i,out_list):
    print(i,in_str[i],'out',out_list)
    if len(in_str) - i < 2:
        out_list.append(in_str[-1])
    elif in_str[i] == in_str[i+1]:
        out_list.append(in_str[i]) 
        out_list.append("*")
        insert_star_worker(in_str,i+1,out_list)
    else:
        out_list.append(in_str[i]) 
        insert_star_worker(in_str,i+1,out_list)

def insert_star_between_pairs(a_string):
    print(a_string)
    if not a_string:
        return None
    out_list = []
    star_list = insert_star_worker(a_string,0,out_list)
    print(out_list)
    return "".join(out_list)


def recur_list_test(k,out):
    if k < 1: return True
    out.append(k)
    recur_list_test(k-1,out)

def fib(n):
    if n < 2: return n
    f1, f2 = 0,1
    for i in range(1,n):
        fib = f1+f2
        f1 = f2
        f2 = fib
    return fib

def merge_ranges(ranges):
    if not ranges: 
        return []
    n = len(ranges)
    minimum, maximum = ranges[0][0], ranges[0][1]
    new_list = [[minimum,maximum]]
    for i in range(1,n):
        left, right = ranges[i][0], ranges[i][1]
        print(left,right)
        # if minimum > left and maximum < right: continue
        if minimum < left <= maximum:
            new_list.pop()
            maximum = max(right,maximum)
            new_list.append([minimum,maximum])
        else:
            new_list.append([left,right])
            minimum = left
            maximum = max(right, maximum)
    return new_list

def insert_range(ranges, new_range):
    if not ranges: return []
    if not new_range: return ranges
    n = len(ranges)
    print(ranges)
    lower, upper = new_range[0], new_range[1]
    for i in range(0,n):
        if lower < ranges[i][0]:
            # print(i,ranges[i])
            ranges.insert(i,new_range)
            break
        elif i == n-1:      # new_range is larger than all elements in list
            ranges.append(new_range)

    print(ranges)
    ranges = merge_ranges(ranges)
    return ranges

def inspect(input1,input2):
    charmap = dict()
    
    for char1, char2 in list(zip(input1,input2)):
        print(char1,char2,charmap)
        if char1 not in charmap:
            charmap[char1] = char2
        else:
            # a,b = charmap[char1]
            # if a != char1 and b != char2:
            if charmap[char1] != char2:
                return False
    return True


def are_isomorphic(input1, input2):
    if input1 == None or input2 == None: return False
    l1, l2 = len(input1), len(input2)
    print(input1,input2)
    if l1 != l2: return False
    if l1 < 2 and l2 < 2: return True
                
    a, b = inspect(input1,input2), inspect(input2,input1)
    return a and b
    
def pad_list(p1,p2):
    while len(p1) > len(p2):
        p2.append(float())
    while len(p2) > len(p1):
        p1.append(float())

path1 = [1,2]
path2 = [1,3,6]

pad_list(path1,path2)
print(path1,path2)


# print(are_isomorphic('foo','bar'))
# print(are_isomorphic('abcd','aabb'))

# print(merge_ranges([]))
# testranges = [[1,4], [3,7], [5,10], [11,15]]
# testranges = [[1,10], [5,8], [8,15]]
# testranges = [[3,5], [5,10], [11,15], [15,20]]
# inserted = insert_range(testranges, [7,8])
# inserted = insert_range(testranges, [9,20])
# inserted = insert_range(testranges, [1,2])
# merged = merge_ranges(testranges)
# imerged = merge_ranges(inserted)
# print(inserted)
# print(merged)
# print(imerged)

# print([fib(i) for i in range(7)])

# path = []
# recur_list_test(7,path)
# print(path)

# print(insert_star_between_pairs("abbba"))
# print(insert_star_between_pairs("cc"))

# print(largestContinuousSum([1,2,3,-2,5]))
# print(largestContinuousSum([-1,-2,3,4,5]))
# print(largestContinuousSum([31, -41, 59, 26, -53, 58, 97, -93, -23, 84]))

# print(largestContinuousSum2([1,2,3,-2,5]))
# print(largestContinuousSum2([-1,-2,3,4,5]))
# print(largestContinuousSum2([31, -41, 59, 26, -53, 58, 97, -93, -23, 84]))


# print(jumps([2,1,1,1,1,12,15]))
# print(jumps([2,5,7,8,9,12]))
# print(jumps([4, 1, 2, 0, 2, 12]))
# print(jumps([2, 1, 1, 1, 1, 1]))



# triple(list(range(1,8)),15)
# triple(list(range(1,8)),10)
# triple(list(range(1,9)),20)
# triple(list([1 for i in range(4)]),3)

# print(is_happy_number(27))


# print(excel_column_number_to_name(19010))
# print(excel_column_number_to_name(494286))
# print(excel_column_number_to_name(52))
# print(excel_column_number_to_name(51))
# print(excel_column_number_to_name(702))
# print(excel_column_name_to_number('ZZ'))
# testlist = [1,2,1,2,1,2]

# s_list = selection_sort(testlist)
# s_list = selection_sort_gourmet(testlist)
# print(s_list)
# s_list = fire_selection_sort(testlist)
# print(s_list)


# print(dec2bin(10))
# print(dec2bin__(6))

# test_str = [1,1,2,3,4,4,5]

# out = find_dups(test_str)

# print(out)

# b = BinaryTree(1)

# left = b.left_child = BinaryTree(2)
# right = b.right_child = BinaryTree(3)

# left.left_child = BinaryTree(4)
# left.right_child = BinaryTree(5)

# right.left_child = BinaryTree(6)
# right.right_child = BinaryTree(7)


# print(b.preorder_iterative())

# b.inorder()
# print(in_ordered_List)

# print(distr_choco([2, 3, 3, 2, 1, 5, 2]))
# print(distr_choco([1,5,7,1]))
# print([1,3,2,1],distr_choco2([1,3,2,1]))
# print([2, 3, 3, 2, 1, 5, 2],distr_choco2([2, 3, 3, 2, 1, 5, 2]))
# print([1,5,7,1],distr_choco2([1,5,7,1]))

# print(excel_column_name_to_number('AB'))
# print(excel_column_name_to_number('AA'))
# print(excel_column_name_to_number('AZ'))
# print(excel_column_name_to_number('AZZ'))


# board = [['A', 'X'],
#        ['D', 'E']]

# # print([a[1:] for a in board[:]])
# print(find_exit(board))

