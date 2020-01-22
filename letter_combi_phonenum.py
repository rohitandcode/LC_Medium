"""
LC 17
return all combinations of letters from phone keypad
ex:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) < 1:
            return None
        given = list(digits) #[2,3]
        dicto={
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        if len(digits) == 1:
            return dicto[given[0]]
        
        #create an empty char list
        res = ['']
        for element in given:
            res = [i+j for i in res for j in dicto[element]]
        return res
