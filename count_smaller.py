import pprint as p
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.smaller = 0
        self.left = None
        self.right = None

# class Solution(object):
def buildBST(nums):
    root = TreeNode(nums[0])
    for i in range(1,len(nums)):
        insertBST(root,nums[i])
    return root

def insertBST(root,x):
    if not root:
        root = TreeNode(x)
        return
    if x >= root.val:
        if not root.right:
            root.right = TreeNode(x)
            return
        return insertBST(root.right,x)
    else:
        root.smaller += 1
        incrAll(root.right)
        if not root.left:
            root.left = TreeNode(x)
            return
        return insertBST(root.left,x)

def incrAll(root):
    if not root: return None
    root.smaller += 1
    if root.left:
        incrAll(root.left)
    if root.right:
        incrAll(root.right)

def BSTgetNode(root,x):
    if not root: return None
    if root.val == x:
        return root
    if root.val > x:
        if root.left:
            return BSTgetNode(root.left,x)
    else:
        if root.right:
            return BSTgetNode(root.right,x)

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
        pre_ordered_List.append((nextnode.val,nextnode.smaller))
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
    util_tree = buildBST(nums)
    # print(nums)
    p.pprint(preorder_iterative(util_tree))
    retlist = [0 for _ in range(len(nums))]
    for i in range(len(nums)):
        print(nums[i])
        node = BSTgetNode(util_tree,nums[i])
        if not node:
            sml = -1
        else:
            sml = node.smaller
        retlist[i] = sml
        # print(retlist)
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

test = [5,2,6,1]
test2 = [26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]
# root = None
# r = buildBST(test)
# insertBST(root,4)
# print(preorder_iterative(r))
# print(countSmaller(test2))
# print(test2)

print(findDups(test2))
test3 = [i for i in test2 if i not in findDups(test2)]
print(test3)

