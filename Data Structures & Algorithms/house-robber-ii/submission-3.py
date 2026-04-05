class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        def rob_simple(houses):
            rob1, rob2 = 0, 0
            for money in houses:
                temp = max(rob1 + money, rob2)
                rob1 = rob2
                rob2 = temp
                
            return rob2
        return max(rob_simple(nums[:-1]), rob_simple(nums[1:]))