import numpy as np

class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = np.array(nums)

    def update(self, index: int, val: int) -> None:
        self.arr[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return np.sum(self.arr[left:right+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)