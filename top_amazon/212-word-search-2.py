"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'
        VISITED = '#'
        
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[WORD_KEY] = word
        
        rows, cols = len(board), len(board[0])
        output = []
        
        def backtrack(i, j, parent):
            if not 0 <= i < rows or not 0 <= j < cols or board[i][j] not in parent:
                return
            
            letter = board[i][j]
            currNode = parent[letter]
            
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                output.append(word_match)
                
            board[i][j] = VISITED   
            
            backtrack(i+1,j, currNode)
            backtrack(i-1,j, currNode)
            backtrack(i,j+1, currNode)
            backtrack(i,j-1, currNode)
            
            board[i][j] = letter
            
            
        for i in range(rows):
            for j in range(cols):
                if board[i][j] in trie:
                    backtrack(i, j, trie)
                
        return output