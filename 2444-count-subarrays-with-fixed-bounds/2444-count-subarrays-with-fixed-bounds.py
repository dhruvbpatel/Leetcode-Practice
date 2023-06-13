class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        min_pos = max_pos = -1
        last_left_out_bound_pos = -1 # idx - start for calculation

        res = 0
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                last_left_out_bound_pos = i
            
            if num == minK:
                min_pos = i
            
            if num == maxK:
                max_pos = i
            
            """
                last_left_out_bound_pos - begin idx subarray
                example 7 0 0 0 1 5 -> 0 0 0 1 5 and 0 0 1 5 and 0 1 5 and 1 5 = 4 res

                so, for escaping such brute force we can calculate min pos (in example it is idx = 4, it is min_elem idx or max_elem_idx)
                min(min_pos, max_pos) begin idx of valid subarray - two cases: 1 2 3 4 5 and 5 4 3 2 1
            """
            res += max(0, min(min_pos, max_pos) - last_left_out_bound_pos)
        
        return res
        