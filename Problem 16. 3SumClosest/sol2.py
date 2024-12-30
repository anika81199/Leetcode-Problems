# using 2-pointer
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = []    # to store difference between target and original sum
        sums = []    # to store original sums
        n = len(nums)
        nums.sort()    

        for i in range(n):
            left = i + 1
            right = n - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                diff.append(abs(target - sum))
                sums.append(sum)

                if sum > target:
                    right -= 1
                elif sum < target:
                    left += 1
                else:
                    return sum

        min_diff_index = diff.index(min(diff))
        return sums[min_diff_index]
