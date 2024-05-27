# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.longest = ""

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def dfs(self, node, path):
        if node.is_end:
            if len(path) > len(self.longest) or (len(path) == len(self.longest) and path < self.longest):
                self.longest = path

            for char in node.children:
                self.dfs(node.children[char], path + char)
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
    
        for char in trie.root.children:
            trie.dfs(trie.root.children[char], char)
        
        return trie.longest
        