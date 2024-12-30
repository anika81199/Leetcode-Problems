# using 2-pointer

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = []
        nums.sort()    # 2-pointer needs sorted array 
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                left = j + 1
                right = len(nums) - 1
                while left < right:     # MOST IMP CONDITION
                    # if nums[i]+nums[j]+nums[left]+nums[right] == 0 and left!=i and left!=j and right!=i and right!=j and i!=j:
                #  A better approach to check if all 4 indices are distinct:-
                    if nums[i]+nums[j]+nums[left]+nums[right] == target and len({i, j, left, right}) == 4:    # set contains distinct elements
                        h = (nums[i], nums[j], nums[left], nums[right])
                        out.append(tuple(sorted(h)))
                        right -= 1
                        left += 1
                    elif nums[i]+nums[j]+nums[left]+nums[right] > target:
                        right -= 1
                    else:
                        left += 1
                      
# removing duplicates from the output
        unique = list(set(out))
        unique_list = [list(x) for x in unique]
        return unique_list 
