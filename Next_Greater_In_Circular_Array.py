class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        max_elem = max(nums)
        n = len(nums)        
        # if array is non-circular, simply initialize empty stack
        stack, result = nums[::-1], [None]*n
        for i in range(n-1,-1,-1):
            if not stack:
                result[i] = max_elem if max_elem != nums[i] else -1
            else: 
                while(stack):
                    if stack[-1] > nums[i]:
                        result[i] = stack[-1]
                        break
                    else:
                        stack.pop()
                if not stack:
                    result[i] = max_elem if max_elem != nums[i] else -1
            stack.append(nums[i])
        return result
