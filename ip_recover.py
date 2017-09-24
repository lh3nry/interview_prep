# ip_recover.py

def generate_ip_address(input):          
    # Return type should be a List.
    def helper(s, index, path, res):
        if index != 4:
            if not s:
                return
        if index == 4:
            if not s:
                res.append(path[:-1])
            return 
        for a in range(1, 4):
            if int(s[:a]) <= 255:
                helper(s[a:], index+1, path + s[:a] + ".", res)
    res = []
    helper(input, 0, "", res)
    return list(set(res))

def generate_ip_address(input):          
    # Return type should be a List.
    ret = set()
    dfs(input, '',ret, 1)
    return list(ret)
    
def dfs(curInput, cur, retVals, number):
    if number == 4 and 0 < len(curInput) <= 3:
        if 0 <= int(curInput) < 256:
            cur += curInput
            retVals.add(cur)
    else:
        if len(curInput) >= 1 and 0 <= int(curInput[:1]) < 256:
            dfs(curInput[1:], cur+ curInput[:1]+'.', retVals, number+1)
        if len(curInput) >= 2 and 0 <= int(curInput[:2]) < 256:
            dfs(curInput[2:], cur+ curInput[:2] +'.', retVals, number+1)
        if len(curInput) >= 3 and 0 <= int(curInput[:3]) < 256:
            dfs(curInput[3:], cur+ curInput[:3] +'.', retVals, number+1)



# class IP_level_node:
#     def __init__(self,pred = None,succ = None,n1 = None,n2 = None,level = 0):
#         self.p_str = pred
#         self.piece1 = n1
#         self.piece2 = n2
#         self.remain = succ
#         self.level = level

#     def check_valid(self):
#         return 0


# # Collections module has already been imported.
# def generate_ip_address(raw_str):
#     # Return type should be a List.
#     stk = [IP_level_node("",raw_str,1)]
#     while True:
#         node = stk.pop(-1)
#         slen = len(node.remain)
#         print(node.remain)
#         # node.p_str += c_str
#         if slen > 3:
#             stk.append(IP_level_node(node.p_str+node.c_str,node.remain[3:],node.remain[0],node.remain[1:2],node.level+1))   # a.bc
#             stk.append(IP_level_node(node.p_str+node.c_str,node.remain[3:],node.remain[0:1],node.remain[2],node.level+1))   # ab.c
#             stk.append(IP_level_node(node.p_str+node.c_str,node.remain[3:],node.remain[0:2],"",node.level+1))               # abc.
#         elif slen == 2:
#             stk.append(IP_level_node(node.p_str+node.c_str,"",node.remain[0],node.remain[1],node.level+1))      # a.b
#             stk.append(IP_level_node(node.p_str+node.c_str,"",node.remain[0:1],"",node.level+1))                # ab.
#             # stk.append(IP_level_node(node.p_str+node.c_str,node.remain[3:],node.remain[0:2]+".",node.level+1))
# Collections module has already been imported.
def generate_ip_address(input):          
    # Return type should be a List. 
    class IpLevelNode:
        def __init__(self,level, ip_to_append, predecessor, successor):
            self.level = level
            self.ip_to_append = ip_to_append
            self.successor = successor
            if level == 0:
                self.predecessor = ip_to_append
            else:
                self.predecessor = str(predecessor) + "." + str(ip_to_append)


    out = []
    stack = collections.deque()
    stack.append(IpLevelNode(0,input[0:1],"", input[1:]))
    stack.append(IpLevelNode(0,input[0:2],"", input[2:]))
    stack.append(IpLevelNode(0,input[0:3],"", input[3:]))
    
    while stack:
        node = stack.popleft()
        curlevel = node.level
        predecessor = node.predecessor
        remaining = node.successor
        if curlevel == 3 and len(remaining) == 0:
            out.append(node.predecessor)
            continue

        i = 1
        while(i <= 3):
            if(len(remaining) < i):
                break
            ipToAppend = remaining[0:i]
            successor = remaining[i:]
            if(len(ipToAppend) > 0):
                numIpToAppend = int(ipToAppend)
            if(numIpToAppend <= 255):
                stack.appendleft(IpLevelNode(curlevel+1,ipToAppend,predecessor,successor))
          
            i+=1

    return out