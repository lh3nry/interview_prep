# btree.py
from functools import reduce
from pprint import pprint
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

    def inorder_itr1(self):
        path = []
        q = [self]
        print('init q:',[node.data for node in q])
        while len(q) > 0:
            # print('before',[node.data for node in q],'path',path)
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

    def inorder_itr2(self):
        path = []
        q = []
        node = self
        # print('init q:',[node.data for node in q])
        while True:
            # print('before',[node.data for node in q],'path',path)
            while node:
                q.append(node)
                node = node.left_child

            if len(q) < 1:
                break;
            node = q.pop(-1)
            path.append(node.data)
            node = node.right_child
            # print('after',[node.data for node in q])
        return path

    def inorder_iter3(self):
        inorder_list = []
        stack = []
        node = self
        while stack or node:
            if node:
                stack.append(node)
                node = node.left_child
            else:
                item = stack.pop()
                inorder_list.append(item.data)
                node = item.right_child
        return inorder_list

    def inorder_iter4(self,root,k):
        inorder_list = []
        q = []
        node = root
        while q or node:
            if node:
                q.append(node)
                node = node.left_child
            else:
                node = q.pop()
                inorder_list.append(node)
                node = node.right_child
        return inorder_list[-k-1]
        
    def validate_bst(self):
        # Return type should be Boolean
        path = []
        q = []
        node = self
        # Do inorder traversal. The order of a BST should be sorted this way        
        while True: 
            # print('before',[node.data for node in q],'path',path)
            while node:         # Head straight to the left most node in each subtree
                q.append(node)
                node = node.left_child

            if len(q) < 1:      # stop if the stack is empty
                break;
                
            node = q.pop(-1)
            if len(path) > 0:
            #   check whether current data is greater than previous nodes
            #   the reduce should return True if the path is monotonically increasing
                if not reduce((lambda x,y: x and y),list(map((lambda x: x<node.data),path))):
                    return False
            path.append(node.data)
            node = node.right_child
        return True

    def validate_bst2(self,root):
        # Return type should be Boolean
        path = []
        q = []
        node = root
        # Do inorder traversal. The order of a BST should be sorted this way        
        while True: 
            # print('before',[node.data for node in q],'path',path)
            while node:         # Head straight to the left most node in each subtree
                q.append(node)
                node = node.left_child

            if len(q) < 1:      # stop if the stack is empty
                break;
                
            node = q.pop(-1)
        
            path.append(node.data)
            node = node.right_child
        
        #   Since the inorder traversed list should be sorted (in a BST),
        #   the reduce statement should return True if the path is monotonically increasing
        # print( list(map( (lambda x,y: x<y), path, path[1:]) ) )
        return reduce( (lambda x,y: x and y), list(map( (lambda x,y: x<y), path, path[1:]) ) )

    def validate_bst3(self,root):
        # Return type should be Boolean
        path = []
        q = []
        node = root
        # Do inorder traversal. The order of a BST should be sorted this way        
        while True: 
            print('path',path)
            while node:         # Head straight to the left most node in each subtree
                q.append(node)
                node = node.left_child

            if not q:      # stop if the stack is empty
                #   Since the inorder traversed list should be sorted (in a BST),
                #   the reduce statement should return True if the path is monotonically increasing
                truth = list(map( (lambda x,y: x<y), path[:-1], path[1:]) )
                # print(truth)
                return reduce( (lambda x,y: x and y), truth )
                
            node = q.pop(-1)
        
            path.append(node.data)
            node = node.right_child

    def find_kth_largest(self,root,k):
        # Return Element should be of type TreeNode
        if k < 1 or not root:
            return None
        q = []
        ordered_list = []
        node = root
    
        while q or node:
            if node:
                q.append(node)
                node = node.left_child
            else:
                node = q.pop()
                ordered_list.append(node)
                node = node.right_child
            
        print([i.data for i in ordered_list])
        return ordered_list[-k]

    def max_node(self,root):
        if not root:
            return None
        q = []
        node = root
        while q or node:
            if node:
                print(node.data)
                q.append(node)
                node = node.right_child
            else:
                node = q.pop()
                print(node.data)
                return node
    
    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.data = obj

    def get_root_val(self):
        return self.data

    def max_sum_path(self,root):
        running_max = [0]
        self.max_sum_worker(root,running_max)
        return running_max[0]

    def max_sum_worker(self,root,r_max):
        if not root:
            return 0

        # Get tallies for both branches
        left = self.max_sum_worker(root.left_child,r_max)
        right = self.max_sum_worker(root.right_child,r_max)

        # Subtree path compare
        # max_subpath = max(max(left,right)+root.data, root.data)

        # Subpath comparison
        # max_root_cmp = max(max_subpath, left+right+root.data)
        max_root_cmp = max(left, right) + root.data

        # update running max (compare with current subtree totals)
        # r_max[0] = max(r_max[0], max_root_cmp)
        r_max[0] = max(r_max[0], left+right+root.data)
        # print('single',max_subpath,'top',max_root_cmp,'running',r_max[0])
        print('root',root.data,'left',left,'right',right,'max_comp',max_root_cmp,'running',r_max[0])
        return max_root_cmp

    def diameter(self,root):
        (md,mh) = self.max_diameter(root)
        # strip the height value from return tuple
        return md
    # Tuple return: (max_diameter, max_height)
    def max_diameter(self,root):
        if not root: return (0,0)
        (ld,lh) = self.max_diameter(root.left_child)
        (rd,rh) = self.max_diameter(root.right_child)
        print('root',root.data,'ld',ld,'rd',rd,'lh',lh,'rh',rh)

        mheight = max(lh,rh) + 1

        return ( max(lh+rh+1, max(ld,rd) ), mheight)

    # def BFSitr(self,root):
    #     if not root: return []
    #     path = []
    #     q = []
    #     node = root
    #     while True:

    def find_path_itr(self,key):
        if self.data == key:
            return [self]
        node = self
        q = [node]
        path = []
        parents = dict()
        while q:
            node = q.pop()
            # print(node.data, [i.data for i in q])
            # print([(i[0],i[1].data) for i in parents.items()])
            if node.data == key:
                n = node
                while n != self:
                    path.insert(0,n)
                    n = parents[n.data]
                    # if n == self: break
                path.insert(0,self)
                return path
            if node.left_child:
                parents[node.left_child.data] = node
                q.append(node.left_child)
            if node.right_child:
                parents[node.right_child.data] = node
                q.append(node.right_child)
        return []

    def find_path(self,root,path,key):
        if not root: return False
        path.append(root)
        print(root.data,[i.data for i in path])

        if root == key:
            return True

        if ( (root.left_child  and self.find_path(root.left_child,path,key) ) or 
             (root.right_child and self.find_path(root.right_child,path,key) ) ):
            return True

        path.pop()
        return False

    def LCA(self,x,y):
        pathx = self.find_path_itr(x)
        pathy = self.find_path_itr(y)
        print('pathx', [i.data for i in pathx])
        print('pathy', [i.data for i in pathy])


        lx = len(pathx)
        ly = len(pathy)

        if lx < 1 or ly < 1:
            return None
        if lx == 1:
            return pathx[0]
        if ly == 1:
            return pathy[0]

        for i in range(min(lx,ly)):        # take the shorter list size
            print(i)
            if pathx[i].data != pathy[i].data:
                lca = pathx[i-1]
                break
        if lx < ly:
            lca = pathy[i]
        elif ly < lx:
            lca = pathx[i]

        # somehow paths aren't connected
        return None

    def get_dist(self,node1_key,node2_key):
        path1 = self.find_path_itr(node1_key)
        path2 = self.find_path_itr(node2_key)
        print('path1', [i.data for i in path1])
        print('path2', [i.data for i in path2])
        dist1, dist2 = len(path1), len(path2)

        if dist1 == 1:
            return dist2
        if dist2 == 1:
            return dist1

        # determine lowest common ancestor
        for i in range(min(dist1,dist2)):        # take the shorter list size
            print(i)
            if path1[i].data != path2[i].data:
                lca = path1[i-1]
                break
        if dist1 < dist2:
            lca = path2[i]
        elif dist2 < dist1:
            lca = path1[i]

        print(dist1,dist2,'lca',lca.data)
        path_lca = self.find_path_itr(lca.data)

        dist_lca = len(path_lca)

        return dist1 + dist2 - 2*dist_lca

    def level_order(self,root,level,retlist):
        if not root:    # empty input
            return None
        # print(root.data)

        if level < 0:   # stop if we went too deep
            return None
        # pass up the node data; we're on the correct level
        if level == 0: 
            retlist.append(root.data)
            return
            # return root.data

        # recurse into left subtree
        left = self.level_order(root.left_child,level-1,retlist)
        # append to list only if the return value exists
            # moved append into "level == 0" condition
        # if left: retlist.append(left)

        # repeat for right subtree
        right = self.level_order(root.right_child,level-1,retlist)
        # if right: retlist.append(right)

    def find_height(self,root):
        if not root: return 0

        return max(self.find_height(root.left_child), self.find_height(root.right_child)) + 1

b = BinaryTree(1)

left = b.left_child = BinaryTree(2)
right = b.right_child = BinaryTree(3)

left.left_child = BinaryTree(4)
left.right_child = BinaryTree(5)

right.left_child = BinaryTree(6)
right.right_child = BinaryTree(7)



# LO0 = []
# b.level_order(b,0,LO0)
# print(LO0)
# LO1 = []
# b.level_order(b,1,LO1)
# print(LO1)
# LO2 = []
# b.level_order(b,2,LO2)
# print(LO2)

b_height = b.find_height(b)

for i in range(b_height):
    levels = []
    b.level_order(b,i,levels)
    print(levels)

# b.find_path_itr(8)
# print([i.data for i in b.find_path_itr(5)])

# somepath = []
# print(type(b))
# b.find_path(b,somepath,5)
# print([i.data for i in somepath])
# print(somepath)

# anc = b.LCA(5,1)
# if anc:
#     print('LCA',anc.data)
# else:
#     print('Paths not connected')

# print(b.get_dist(4,2))



#         1
#      2      3
#   4   5   6   7

# print(b.find_kth_largest(b,2).data)
# print(b.inorder_iter4(b,2).data)

# print(b.preorder_iterative())

# b.inorder()
# print(in_ordered_List)

# print(b.inorder_itr1())
# print(b.inorder_itr2())

# print(b.validate_bst())

# b2 = BinaryTree(20)
# b2.left_child = BinaryTree(15)
# b2.left_child.left_child = BinaryTree(10)
# b2.right_child = BinaryTree(40)
# b2.right_child.left_child = BinaryTree(30)

# print(b2.validate_bst())
# print(b.max_node(b2).data)

# b3 = BinaryTree(20)
# b3.left_child = BinaryTree(15)
# b3.left_child.left_child = BinaryTree(10)
# b3.right_child = BinaryTree(40)
# b3.left_child.right_child = BinaryTree(30)

# print(b3.validate_bst())
# print(b3.validate_bst2(b3))

# b4 = BinaryTree(3)
# b4.left_child = BinaryTree(2)
# b4.right_child = BinaryTree(4)

# print(b.validate_bst2(b4))

# b5 = BinaryTree(20)
# b5.left_child = BinaryTree(15)
# b5.left_child.right_child = BinaryTree(18)
# b5.right_child = BinaryTree(30)
# b5.right_child.right_child = BinaryTree(40)

# print(b.validate_bst2(b5))

# bmax = BinaryTree(1)
# bmax.left_child = BinaryTree(2)
# bmax.left_child.left_child = BinaryTree(4)
# bmax.left_child.right_child = BinaryTree(5)
# bmax.right_child = BinaryTree(3)
# bmax.right_child.left_child = BinaryTree(6)
# bmax.right_child.right_child = BinaryTree(7)

# print(b.max_sum_path(bmax))


bdiam = BinaryTree(20)
bdiam.left_child = BinaryTree(15)
bdiam.left_child.left_child = BinaryTree(14)
bdiam.left_child.right_child = BinaryTree(18)
bdiam.left_child.right_child.left_child = BinaryTree(17)
bdiam.left_child.right_child.right_child = BinaryTree(19)
bdiam.right_child = BinaryTree(30)
bdiam.right_child.right_child = BinaryTree(35)
bdiam.right_child.right_child.left_child = BinaryTree(32)

# bdiam2 = BinaryTree(1)
# bdiam2.left_child = BinaryTree(2)
# bdiam2.left_child.left_child = BinaryTree(4)
# bdiam2.left_child.right_child = BinaryTree(5)
# bdiam2.right_child = BinaryTree(3)

# print(b.max_diameter(bdiam))
# print(b.max_diameter(bdiam2))

# print(bdiam.get_dist(20,35))
# print([i.data for i in bdiam.find_path_itr(35)])
# print([i.data for i in bdiam.find_path_itr(18)])


# print(bdiam.LCA(17,35).data)










