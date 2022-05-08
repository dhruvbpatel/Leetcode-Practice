class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        sum = 0
        for i in nums:
            sum+=i
            maxi = max(maxi,sum)
            sum = max(0,sum)
        return maxi
        