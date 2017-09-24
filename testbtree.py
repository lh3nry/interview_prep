# testbtree.py

class TreeNode:
    def __init__(self, data,left_child = None, right_child = None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
    
    def __str__(self):
        return '%s' %self.data

class BinaryTree:
    
    def __init__(self, root_node = None):
        # Check out Use Me section to find out Node Structure
        self.root = root_node
    
    def find_path(self,root,key):
        if root.data == key:
            return [root]
        node = root
        q = [node]
        path = []
        parents = dict()
        while q:
            node = q.pop()
            # print(node.data, [i.data for i in q])
            # print([(i[0],i[1].data) for i in parents.items()])
            if node.data == key:
                n = node
                while n != root:
                    path.insert(0,n)
                    n = parents[n.data]
                path.insert(0,root)
                return path
            if node.left_child:
                parents[node.left_child.data] = node
                q.append(node.left_child)
            if node.right_child:
                parents[node.right_child.data] = node
                q.append(node.right_child)
        return []
    
    def find_path(self,key):
        # print(key)
        if self.root.data == key.data:
            return [self.root]
        node = self.root
        q = [node]
        parents = dict()
        path = []
        
        while q:
            node = q.pop()
            # print(node.data, [i.data for i in q])
            # print([(i[0],i[1].data) for i in parents.items()])
            if node.data == key.data:
                # print('found key')
                # we reconstruct the path using our hashed set 
                # which stores parents using a node index
                n = node
                while True:
                    path.insert(0,n)
                    n = parents[n.data]     # find the next parent
                        # "do-while" continue path finding until we reach the root
                    if n == self.root:      
                        path.insert(0,self.root)    # insert the root
                        # print([i.data for i in path])
                        return path
            if node.left_child:
                # Store node as the parent of the left_child before proceeding
                parents[node.left_child.data] = node
                q.append(node.left_child)
            if node.right_child:
                parents[node.right_child.data] = node
                q.append(node.right_child)
                
        # if we got here ( emptied stack ), we did a full traversal 
        # and did not find the key
        return []
    
    def findLCA(self,root,node_a, node_b):
        # Return type should be of type TreeNode
        if not root:
            return None
        # if not (node_a.data == 1 and node_b.data == 2):
        #     return None
        print('a',node_a.data,'b',node_b.data)

        if not root.left_child and not root.right_child:
            return root
        path_a = self.find_path(node_a)
        path_b = self.find_path(node_b)
        print([i.data for i in path_a],[i.data for i in path_b])
        
        na, nb = len(path_a), len(path_b)
        
        
        for i in range(min(na,nb)):
            if path_a[i] != path_b[i]:
                # print(path_a[i-1])
                return path_a[i-1]
        return path_a[i]
  

        
    def pad_list(p1,p2):
        # print(type(p1[0]))
        n = TreeNode(0)
        while len(p1) > len(p2):
            p2.append(n)
        while len(p2) > len(p1):
            p1.append(n)
        
    def get_node_distance(self,root,node_data1,node_data2):
        # if not (node_data1 == 2 and node_data2 == 5): return 0
        # print('n1',node_data1,'n2',node_data2)
        path1 = self.find_path(root,node_data1)
        path2 = self.find_path(root,node_data2)
        print('path1', [i.data for i in path1])
        print('path2', [i.data for i in path2])
        dist1, dist2 = len(path1), len(path2)
        # print('d1',dist1,'d2',dist2,'path1',path1[0].data)
        if dist1 < 2 or dist2 < 2:
            # print('n1',node_data1,'n2',node_data2)
            lca = path1[0]
        else:
            if dist1 != dist2:
                # self.pad_list(path1,path2)
                n = TreeNode(0)
                while len(path1) > len(path2):
                    path2.append(n)
                while len(path2) > len(path1):
                    path1.append(n)
            print('path1', [i.data for i in path1])
            print('path2', [i.data for i in path2])
            for i in range(len(path1)):
                if path1[i].data != path2[i].data:
                    lca = path1[i-1]
                    break
                
        print(lca)
        if lca.data == root.data: dist_lca = 1
        else:
            path_lca = self.find_path(root,lca.data)
            # print('path_lca', [i.data for i in path_lca])
            dist_lca = len(path_lca)
        return dist1 + dist2 - 2*dist_lca


t = TreeNode(1)
t.left_child = TreeNode(2)
t.right_child = TreeNode(3)

b = BinaryTree(t)

node = b.findLCA(t,TreeNode(2),TreeNode(3))

print(node.data)