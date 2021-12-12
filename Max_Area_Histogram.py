class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left, right = [], []        
        n = len(heights)
        def nsr(nums) -> List:
            stack = []
            result = [None]*len(nums)
            for i in range(n-1, -1, -1):
                if not stack:
                    result[i] = n
                else:
                    while stack:
                        if stack[-1][0] < nums[i]:
                            result[i] = stack[-1][1]
                            break
                        else:
                            stack.pop()
                    if not stack:
                        result[i] = n                        
                stack.append((nums[i], i))
            return result
                            
        def nsl(nums) -> List:
            stack = []
            result = [None]*len(nums)
            for i in range(0, n):
                if not stack:
                    result[i] = -1
                else:
                    while stack:
                        if stack[-1][0] < nums[i]:
                            result[i] = stack[-1][1]
                            break
                        else:
                            stack.pop()
                    if not stack:
                        result[i] = -1                       
                stack.append((nums[i], i))
            return result
                             
        right = nsr(heights)
        left = nsl(heights)
        print(left)
        print(right)
        width = [right[i]-left[i]-1 for i in range(n)]
        print(width)
        max_area = -9999
        for i in range(n):
            if heights[i]*width[i]>max_area:
                max_area = heights[i]*width[i]
        return max_area
