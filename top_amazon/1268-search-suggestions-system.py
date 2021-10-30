"""
Given an array of strings products and a string searchWord. We want to design a system that suggests at most three 
product names from products after each character of searchWord is typed. Suggested products should have common prefix 
with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed. 

Example 1:
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

Example 2:
Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

Example 3:
Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]

Example 4:
Input: products = ["havana"], searchWord = "tatiana"
Output: [[],[],[],[],[],[],[]]
 
Constraints:

1 <= products.length <= 1000
There are no repeated elements in products.
1 <= Σ products[i].length <= 2 * 10^4
All characters of products[i] are lower-case English letters.
1 <= searchWord.length <= 1000
All characters of searchWord are lower-case English letters.
"""
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        self.ans = []
        self.initializeTrie(products)
        
        for i in range(len(searchWord)):
            prefix = searchWord[0:i+1]
            self.ans.append(self.getWordsFromTrie(prefix))
        
        return self.ans
    
    def initializeTrie(self, words):
        self.trie = {}
        for word in words:
            node = self.trie
            for letter in word:
                node = node.setdefault(letter, {})
            node['#'] = word
    
    def getWordsFromTrie(self, prefix):
        node = self.trie
        for letter in prefix:
            if letter in node:
                node = node[letter]
            else:
                return []
        
        def dfs(node, found):
            if '#' in node:
                found.append(node['#'])
            for letter in node:
                if letter == '#': continue
                dfs(node[letter], found)
            
        found = []
        dfs(node, found)
        
        found.sort()
        return found[0:3]

# n = len(products)
# m = max([len(p) for p in products])
# p = len(searchWord)
# time: sort(m*n*log(n)) + searchInTrie(p(p+1)/2)) + buildTrie(n*m)
# space: numberNodes * 26 
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        self.ans = []
        products.sort()
        self.initializeTrie(products)
        
        for i in range(len(searchWord)):
            prefix = searchWord[0:i+1]
            self.ans.append(self.getWordsFromTrie(prefix))
        
        return self.ans
    
    def initializeTrie(self, words):
        self.trie = {}
        for word in words:
            node = self.trie
            for letter in word:
                node = node.setdefault(letter, {})
                
                if '#' in node: 
                    if len(node['#']) < 3:
                        node['#'].append(word)
                else:
                    node['#'] = [word]    
        
    def getWordsFromTrie(self, prefix):
        node = self.trie
        for letter in prefix:
            if letter in node:
                node = node[letter]
            else:
                return []
        return node['#']

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        
        ans = []
        curr, runner = 0, 0
        
        while runner < len(products) and curr < len(searchWord):
            if len(products[runner]) < curr+1 or products[runner][curr] < searchWord[curr]:
                runner += 1  
            elif products[runner][curr] == searchWord[curr]:
                options = []
                for product in products[runner: runner + 3]:
                    if product[0:curr+1] == searchWord[0:curr+1]:
                        options.append(product)
                ans.append(options)
                curr += 1
            else:
                break
                
        while curr < len(searchWord):
            ans.append([])
            curr+=1
        
        return ans

# n = len(products)
# m = max([len(p) for p in products])
# p = len(searchWord)
#time: O(m * n * log(n) + (n + p)) = O(m*n*log(n)) 
#space: O(1)

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products.sort()
        
        m = len(searchWord)
        left, right = 0, len(products) - 1
        i = 0
        
        suggestions = [[] for _ in range(m)]
        
        while left <= right and i < m:
            
            if len(products[left]) <= i or products[left][i] != searchWord[i]:
                left += 1
                continue
                
            if len(products[left]) <= i or products[right][i] != searchWord[i]:
                right -= 1
                continue
            
            end = min(left + 3, right + 1)
            for j in range(left, end):
                suggestions[i].append(products[j])
                
            i += 1
        
        return suggestions