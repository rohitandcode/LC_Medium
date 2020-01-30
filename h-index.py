# LC 274: https://leetcode.com/problems/h-index/submissions/


"""With enumerate, we can print the index like this: (for input [3,0,6,1,5])
index, citation_value
(0, 6)
(1, 5)
(2, 3)
(3, 1)
(4, 0)
so, we look for a condition where citation value is greater than index.
if it is, then we update "h" value with it.
"""

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h=0
        if len(citations) == 1:
            if citations[0] == 0:
                return 0
            return 1
        citations=sorted(citations, reverse=True)
        for index, cited in enumerate(citations):
            print (index,cited)
            if cited > index:
                h = index+1
        return h
