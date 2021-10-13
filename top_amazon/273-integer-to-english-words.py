"""
Convert a non-negative integer num to its English words representation.

 

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: num = 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
 

Constraints:

0 <= num <= 231 - 1"""

class Solution:
    def numberToWords(self, num: int) -> str:
        one = {
            0:"Zero",
            1:"One",
            2:"Two",
            3:"Three",
            4:"Four",
            5:"Five",
            6:"Six",
            7:"Seven",
            8:"Eight",
            9:"Nine"
        }
        
        two_less_20= {
            10:"Ten",
            11:"Eleven",
            12:"Twelve",
            13:"Thirteen",
            14:"Fourteen",
            15:"Fifteen",
            16:"Sixteen",
            17:"Seventeen",
            18:"Eighteen",
            19:"Nineteen"
        }  
        
        ten = {
            20:"Twenty",
            30:"Thirty",
            40:"Forty",
            50:"Fifty",
            60:"Sixty",
            70:"Seventy",
            80:"Eighty",
            90:"Ninety"
        } 
        
        def two(num):
            if num < 10:
                return one[num]
            elif num < 20:
                return two_less_20[num]
            else:
                rest = num % 10
                tenner = num - rest
                word = ten[tenner]
                if rest:
                    word = word + " " + one[rest]
                return word
                      
        def three(num):
            hundred = num//100
            rest = num % 100
            
            if hundred and rest:
                return one[hundred] + " Hundred " + two(rest)
            if not hundred and rest:
                return two(rest)
            if hundred and not rest:
                return one[hundred] + " Hundred"
        
        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000
        
        if not num:
            return 'Zero'
        
        result = ''
        if billion:
            result = three(billion) + " Billion"
        if million:
            result += ' ' if result else ''    
            result += three(million) + ' Million'
        if thousand:
            result += ' ' if result else ''
            result += three(thousand) + ' Thousand'
        if rest:
            result += ' ' if result else ''
            result += three(rest)
        return result