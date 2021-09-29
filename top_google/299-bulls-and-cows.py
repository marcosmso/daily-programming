"""
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is.
When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong 
position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

Example 1:
Input: secret = "1807", guess = "7810"
Output: "1A3B"

Example 2:
Input: secret = "1123", guess = "0111"
Output: "1A1B"

Example 3:
Input: secret = "1", guess = "0"
Output: "0A0B"

Example 4:
Input: secret = "1", guess = "1"
Output: "1A0B"

"""

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        seen_secret, seen_guess = 10 * [0], 10 * [0]
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                seen_secret[int(secret[i])] += 1
                seen_guess[int(guess[i])] += 1 
        
        for i in range(len(seen_secret)):
            cows += min(seen_secret[i], seen_guess[i])
            
        return "{}A{}B".format(bulls, cows)

# class Solution:
#     def getHint(self, secret: str, guess: str) -> str:
#         h = defaultdict(int)
#         bulls = cows = 0

#         for idx, s in enumerate(secret):
#             g = guess[idx]
#             if s == g: 
#                 bulls += 1
#             else:
#                 cows += int(h[s] < 0) + int(h[g] > 0)
#                 h[s] += 1
#                 h[g] -= 1
                
#         return "{}A{}B".format(bulls, cows)