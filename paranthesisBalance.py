"""
921. Minimum Add to Make Parentheses Valid
    Input: "())"
    Output: 1
    
    Input: "()))(("
    Output: 4 """
    """
    Understanding:
    So, to solve this, just counting unequal number of left_paran or right_paran and subtracting the 
    difference is not enough, we have to look at cases like the above input. Here, although both
    open and close are equal, output is still 4, because they are not balance.
    
    so, idea is to create a stack(list), where if we see a right_paran[")"], then we check if in
    the stack we have a left_paran["("]. If we don;t see a left_paran then we add right paran to the stack.
    But if we see a left_paran, then we delete(pop) left_paran from stack and ignore right_paran.
 """
     
class Solution(object):
    def paranthesisBalance(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        if len(S) == 0:
            return 0
        for i in S:
            if stack and i == ")" and len(stack) > 0 and stack[-1] == "(":
                stack.pop(-1)
            elif i == "(" or i == ")":
                stack.append(i)
        return (len(stack))
