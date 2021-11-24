"""
TinyURL is a URL shortening service where you enter a URL such as
https://leetcode.com/problems/design-tinyurl and it returns a short 
URL such as http://tinyurl.com/4e9iAk. Design a class to encode a URL
and decode a tiny URL.

There is no restriction on how your encode/decode algorithm should 
work. You just need to ensure that a URL can be encoded to a tiny 
URL and the tiny URL can be decoded to the original URL.

Implement the Solution class:

Solution() Initializes the object of the system.
String encode(String longUrl) Returns a tiny URL for the given longUrl.
String decode(String shortUrl) Returns the original long URL for the given shortUrl. It is guaranteed that the given shortUrl was encoded by the same object.
 
Example 1:
Input: url = "https://leetcode.com/problems/design-tinyurl"
Output: "https://leetcode.com/problems/design-tinyurl"

Explanation:
Solution obj = new Solution();
string tiny = obj.encode(url); // returns the encoded tiny url.
string ans = obj.decode(tiny); // returns the original url after deconding it.
 
Constraints:

1 <= url.length <= 104
url is guranteed to be a valid URL.
"""
class Codec:
    def __init__(self):
        self.urlID = 0
        self.shortToLong = {}
        self.longToShort = {}
        self.letters ="abcdefghijklmnopqrstuvxwyzABCDEGGHIJKLMNOPQRSTUVXWYZ0123456789"
        self.base = 62
        self.urlLength = 7
    
    def encode(self, longUrl: str) -> str:
        if not longUrl and len(longUrl) == 0:
            return None
        if longUrl in self.longToShort:
            return self.longToShort[longUrl]
        
        digits = self.convertBase(self.urlID, self.base)
        self.urlID +=1
        
        shortUrl = []
        for digit in digits:
            shortUrl.append(self.letters[digit])
        shortUrl = "".join(shortUrl)
        
        self.shortToLong[shortUrl] = longUrl
        self.longToShort[longUrl] = shortUrl
        
        return shortUrl
        
    def convertBase(self, num, base):
        if num == 0:
            return self.urlLength *[0]
        
        digits = []
        while num > 0:
            remain = num % base
            num = num // base
            digits.append(remain)
            
        digits.reverse()
        digits = (self.urlLength-len(digits))*[0] + digits
        return digits      

    def decode(self, shortUrl: str) -> str:
        if not shortUrl or len(shortUrl) == 0:
            return None
        return self.shortToLong[shortUrl] if shortUrl in self.shortToLong else None
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))