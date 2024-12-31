# using 2-pointers --> sorted array isn't necessary for the algo
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0        # any area will be bigger than this
        
        while left < right:
            width = right - left
            length = min(height[left], height[right])
            curr_area = length * width
            max_area = max(max_area, curr_area)
            
            # Moving the pointer corresponding to the smaller height inwards
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
