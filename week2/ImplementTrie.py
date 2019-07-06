class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isWord = False
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        
        cur_node = self.root
        for i in range(len(word)):
            node_index = ord(word[i])-ord('a')
            #if node already exists
            if cur_node.children[node_index]:
                cur_node = cur_node.children[node_index]
            else:
                cur_node.children[node_index] = TrieNode()
                cur_node = cur_node.children[node_index]
        
        cur_node.isWord = True
            
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur_node = self.root
        for i in range(len(word)):
            node_index = ord(word[i])-ord('a')
            #if node already exists
            if cur_node.children[node_index]:
                cur_node = cur_node.children[node_index]
            else:
                return False
            
        if cur_node.isWord:
            return True

        return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur_node = self.root
        for i in range(len(prefix)):
            node_index = ord(prefix[i])-ord('a')
            #if node already exists
            if cur_node.children[node_index]:
                cur_node = cur_node.children[node_index]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)