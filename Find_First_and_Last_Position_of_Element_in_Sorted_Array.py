class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(arr, l, r, x):
            while l<=r:
                mid = l + (r-l)//2
                if arr[mid] == x:
                    return mid
                elif arr[mid]<x:
                    l = mid+1
                else:
                    r = mid - 1
            return -1
        
        
        target_pos = binary_search(nums, 0, len(nums)-1, target)
        print(target_pos)
        if target_pos == -1:
            return [-1,-1]
        
        left = target_pos
        right = target_pos
        # final_left = target
        # final_right = target
        while((left-1)>=0 and nums[left-1]==target):
            left = left - 1
        while((right+1)<len(nums) and nums[right+1]==target):
            right = right+1
        return [left,right]
