# Problem: Path Sum III - https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return self.helper(root,targetSum,[])
    def helper(self,curNode ,targetSum,curPath):
        if curNode is None:
            return 0
        
        curPath.append(curNode.val)
        pCount , pSum = 0 , 0

        for i in range(len(curPath)-1,-1,-1):
            pSum += curPath[i]

            if pSum == targetSum:
                pCount +=1
        
        pCount += self.helper(curNode.left,targetSum,curPath)
        pCount += self.helper(curNode.right,targetSum,curPath)

        del curPath[-1]

        return pCount
        