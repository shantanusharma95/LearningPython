'''
Implement "TRIE” data structure from scratch with the following functions.

Trie(): Initialize the object of this “TRIE” data structure.
insert(“WORD”): Insert the string “WORD” into this “TRIE” data structure.
countWordsEqualTo(“WORD”): Return how many times this “WORD” is present in this “TRIE”.
countWordsStartingWith(“PREFIX”): Return how many words are there in this “TRIE” that have the string “PREFIX” as a prefix.
erase(“WORD”): Delete one occurrence of the string “WORD” from the “TRIE”.

https://takeuforward.org/plus/dsa/problems/trie-implementation-and-advanced-operations

'''

class Node:
    def __init__(self, val, eow=False):
        self.val = val
        self.eow = eow    #to indicate completion of word
        self.count = 0      #to keep record of how many times a char occurs
        self.children = {}  #char to Node mapping for children

class Trie:
    def __init__(self):
        self.head = Node(0)

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curNode = self.head
        n = len(word)
        for i, ch in enumerate(word):
            if ch in curNode.children:
                curNode = curNode.children[ch]
                curNode.count+=1
            else:
                newNode = Node(ch, eow=i==n-1)
                curNode.children[ch] = newNode
                curNode = curNode.children[ch]
                curNode.count+=1

    def countWordsEqualTo(self, word):
        """
        :type word: str
        :rtype: int
        """
        curNode = self.head
        n = len(word)
        for i, ch in enumerate(word):
            if ch in curNode.children:
                curNode = curNode.children[ch]
                if i==n-1:
                    return curNode.count if curNode.eow else 0
            else:
                return 0

    def countWordsStartingWith(self, prefix):
        """
        :type word: str
        :rtype: int
        """
        curNode = self.head
        n = len(prefix)
        for i, ch in enumerate(prefix):
            if ch in curNode.children:
                curNode = curNode.children[ch]
                if i==n-1:
                    return curNode.count
            else:
                return 0
        

    def erase(self, word):
        """
        :type word: str
        :rtype: None
        """
        curNode = self.head
        par = None
        n = len(word)
        for i, ch in enumerate(word):
            if ch in curNode.children:
                par = curNode
                curNode = curNode.children[ch]
                if curNode.count==1:
                    del par.children[ch]
                    return
                curNode.count-=1
                par=curNode

                
                    
##Sample Call-
obj = Trie()
w1="hello"
w2="help"
w3="help"
obj.insert(w1)
obj.insert(w2)
obj.insert(w3)
print(obj.countWordsEqualTo(w2))
print(obj.countWordsStartingWith("he"))
obj.erase(w2)
print(obj.countWordsEqualTo(w2))

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
