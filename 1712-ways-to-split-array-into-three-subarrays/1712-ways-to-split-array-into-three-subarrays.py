class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1]+num)
        # prefix[i] <= prefix[j]-prefix[i] <= prefix[-1]-prefix[j]
        # => prefix[i]*2 <= prefix[j] <= (prefix[-1]+prefix[i])/2
        # find the range of j: lower <= j < upper
        ways = 0
        lower = upper = 0
        for i in range(1, len(prefix)-2):
            # lower = lower bound of j
            lower = max(lower, i+1) # i+1 <= lower
            while lower < len(prefix)-1 and prefix[lower] < prefix[i]*2: # prefix[i]*2 <= prefix[j]
                lower += 1
            # upper = (upper bound of j) + 1
            upper = max(upper, lower) # lower < upper
            while upper < len(prefix)-1 and prefix[upper] <= (prefix[-1]+prefix[i])/2: # prefix[j] <= (prefix[-1]+prefix[i])/2
                upper += 1
            ways += upper - lower
        return ways % (10**9+7)