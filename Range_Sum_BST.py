# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int, sum_ = 0) -> int:        
        if not root:
            return 0
        if low <= root.val <= high:
            sum_ = sum_ + root.val
        if root.val >= low:
            sum_ = sum_ + self.rangeSumBST(root.left, low, high)
        if root.val <= high:
            sum_ =  sum_ +  self.rangeSumBST(root.right, low, high)
        return sum_
