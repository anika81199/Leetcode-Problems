# using 2-pointer
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
       
        closest_sum = float('inf')   # compare with infinity so that any sum will be less than this value
        n = len(nums)
        nums.sort()

        for i in range(n):
            left = i + 1
            right = n - 1

            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if abs(cur_sum - target) < abs(closest_sum - target):
                    closest_sum = cur_sum
                if cur_sum == target:
                    return cur_sum
                elif cur_sum < target:
                    left += 1
                else:
                    right -= 1
        return closest_sum
