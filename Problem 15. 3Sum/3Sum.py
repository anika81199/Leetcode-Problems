# using Two-pointer algo
# Time: O(n^2)
# Space: O(k), unique triplets
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()     # two-pointer needs sorted array
        out = []

        for i in range(len(nums)):
            left = i + 1             # instead of starting left from index 0, start from i+1
            right = len(nums) - 1
            while left < right:
                if nums[left]+nums[right]+nums[i]==0:
                    out.append((nums[left], nums[right], nums[i]))
# now this triplet is recorded we need to squeeze left & right indices inwards to record new triplets
                    left += 1
                    right -= 1
                elif nums[left]+nums[right]+nums[i]>0:
                    right -= 1
                else:
                    left += 1

        # to remove duplicates
        unique = set(out)
        unique_list = [list(x) for x in unique]
        return unique_list 
