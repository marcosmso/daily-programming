
"""
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
Return any possible rearrangement of s or return "" if not possible.

Example 1:
Input: s = "aab"
Output: "aba"

Example 2:
Input: s = "aaab"
Output: ""
 
Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
"""

import collections
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = collections.Counter(s)
        queue = []
        
        for letter, freq in counter.items():
            heapq.heappush(queue, (-1* freq, letter)) # max heap
        
        string = []   
        while len(queue) > 1:
            _, letter1 = heapq.heappop(queue)
            _, letter2 = heapq.heappop(queue)

            string.append(letter1)
            string.append(letter2)
            
            counter[letter1] -= 1
            counter[letter2] -= 1
            
            if counter[letter1] > 0:
                heapq.heappush(queue, (-counter[letter1], letter1))    
            if counter[letter2] > 0:
                heapq.heappush(queue, (-counter[letter2], letter2))
                
        if len(queue) == 1:
            freq, letter = heapq.heappop(queue)
            if -freq > 1:
                return ""
            string.append(letter)
        
        return "".join(string)

class Solution(object):
    def reorganizeString(self, s):    
        frequencies = collections.Counter(s) 
        
        sorted_freq = [(freq, char) for char, freq in frequencies.items()]
        sorted_freq.sort(reverse=True)
        
        sorted_str = []
        for freq, ch in sorted_freq:
            sorted_str += freq * [ch]
        
        i = 0
        j = len(sorted_str)//2
        add_middle_char = False
        if len(sorted_str) % 2 == 1:
            j += 1
            add_middle_char = True
            
        if sorted_str[i] == sorted_str[j]:
            return ""
        
        to_return = []
        while j < len(sorted_str):
            to_return.append(sorted_str[i])
            to_return.append(sorted_str[j])
            i += 1
            j += 1
        
        if add_middle_char:
            to_return.append(sorted_str[i])
        
        return "".join(to_return)