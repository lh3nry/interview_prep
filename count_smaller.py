import pprint as p
class TreeNode:
    def __init__(self, x, i):
        self.val = x
        self.smaller = 0
        self.index = i
        self.left = None
        self.right = None

# class Solution(object):
def buildBST(nums):
    root = TreeNode(nums[0],0)
    for i in range(1,len(nums)):
        insertBST(root,nums[i],i)
    return root

def buildBST2(nums,ret):
    root = TreeNode(nums[0],0)
    for i in range(1,len(nums)):
        insertBST2(root,nums[i],i,ret)
    return root

def insertBST(root,x,i):
    if not root:
        root = TreeNode(x,i)
        return
    if x > root.val:
        if not root.right:
            root.right = TreeNode(x,i)
            return
        return insertBST(root.right,x,i)
    elif x == root.val:
        if not root.right:
            root.right = TreeNode(x,i)
            return
        return insertBST(root.right,x,i)
    else:
        root.smaller += 1
        incrAll(root.right)
        if not root.left:
            root.left = TreeNode(x,i)
            return
        return insertBST(root.left,x,i)

def insertBST2(root,x,i,ret):
    if not root:
        root = TreeNode(x,i)
        return
    if x > root.val:
        if not root.right:
            root.right = TreeNode(x,i)
            return
        return insertBST2(root.right,x,i,ret)
    elif x == root.val:
        if not root.right:
            root.right = TreeNode(x,i)
            return
        return insertBST2(root.right,x,i,ret)
    else:
        root.smaller += 1
        ret[root.index] += 1
        incrAll2(root.right,ret)
        if not root.left:
            root.left = TreeNode(x,i)
            return
        return insertBST2(root.left,x,i,ret)

def incrAll(root):
    if not root: return None
    root.smaller += 1
    if root.left:
        incrAll(root.left)
    if root.right:
        incrAll(root.right)

def incrAll2(root,ret):
    if not root: return None
    root.smaller += 1
    ret[root.index] += 1
    if root.left:
        incrAll2(root.left,ret)
    if root.right:
        incrAll2(root.right,ret)

def BSTgetNode(root,x,i):
    if not root: return None
    if root.val == x:
        if i == root.index:
            return root
        if root.right:
            return BSTgetNode(root.right,x,i)
    if root.val > x:
        if root.left:
            return BSTgetNode(root.left,x,i)
    else:
        if root.right:
            return BSTgetNode(root.right,x,i)

def inorder_iter3(self):
    inorder_list = []
    stack = []
    node = self
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            item = stack.pop()
            inorder_list.append(item.val)
            node = item.right
    return inorder_list

def preorder_iterative(self):
    pre_ordered_List = []
    q = [self]
    while len(q) > 0:
        # print('before',[node.val for node in q])
        nextnode = q.pop()
        pre_ordered_List.append((nextnode.val,nextnode.smaller,nextnode.index))
        # if nextnode.left:
        #   q = [nextnode.left] + q
        # if nextnode.right:
        #   q = [nextnode.right] + q
        if nextnode.right:
            q.append(nextnode.right)
        if nextnode.left:
            q.append(nextnode.left)
        # print('after',[node.val for node in q])
    return pre_ordered_List

def countSmaller(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # util_tree = buildBST(nums)
    # print(nums)
    # p.pprint(preorder_iterative(util_tree))
    retlist = [0 for _ in range(len(nums))]
    util_tree = buildBST2(nums,retlist)

    # for i in range(len(nums)):
    #     # print(nums[i])
    #     node = BSTgetNode(util_tree,nums[i],i)
    #     if not node:
    #         sml = -1
    #     else:
    #         sml = node.smaller
    #     retlist[i] = sml
    #     # print(retlist)
    return retlist

def findDups(nums):
    d = dict()
    dups = []
    for x in nums:
        if x not in d:
            d[x] = x
        else:
            dups.append(x)
    return dups

test = [5,2,6,1,5]
test2 = [
    26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41
    ]
# root = None
# r = buildBST(test)
# insertBST(root,4)
# print(preorder_iterative(r))
# print(countSmaller(test))
print(countSmaller(test2))
# t = buildBST(test)
# print(preorder_iterative(t))

# print(test2)

# print(findDups(test2))
# test3 = [i for i in test2 if i not in findDups(test2)]
# print(countSmaller(test3))

'''
[10,27,10,35,12,22,28,8,19,2,12,2,9,6,12,5,17,9,19,12,14,6,12,5,12,3,0,10,0,7,8,4,0,0,4,3,2,0,1,0]
'''

