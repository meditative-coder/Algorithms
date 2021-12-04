class Solution:
    def maxArea(self, height: List[int]) -> int:
        lis = len(height)
        left, right = 0, lis-1
        max_area = 0
        while(left<right):
            area = min(height[left], height[right]) * (right-left)
            max_area = max(max_area, area)
            if height[left]<height[right]:
                left = left + 1
            else:
                right = right - 1
        return max_area
