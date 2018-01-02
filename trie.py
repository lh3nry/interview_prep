# trie.py

class TrieNode:
    def __init__(self):
        self.data = None
        self.count = 0
        self.next = {}
        
    def insert(self,wd):
        node = self
        # update the root node counter 
        # (each insert adds a new word)
        node.count+=1

        for ch in wd:
            if ch not in node.next:
                new = TrieNode()
                new.data = ch
                new.count = 1
                node.next[ch] = new
                node = node.next[ch]
            else:
                node = node.next[ch]
                node.count += 1

    def find(self, wd):
        node = self
        for ch in wd:
            if ch not in node.next: return 0
            node = node.next[ch]
        return node.count



test = "hackerrank"

tn = TrieNode()

tn.insert(test)
tn.insert("hack")
# print(tn.count)
# print(tn.find("hackerra"))
print(tn.find("hac"))
print(tn.find("hak"))
print(tn.find("hacker"))