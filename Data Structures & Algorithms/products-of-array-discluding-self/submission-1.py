class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productArr = []
        leftProduct = [1]
        rightProduct = [1]   

        curr = 1
        for i in nums[:-1]:
            curr = curr * i
            leftProduct.append(curr)

        curr = 1
        for i in nums[:0:-1]:
            curr = curr * i
            rightProduct.append(curr)

        n = len(nums)
        for i in range(n):
            res = leftProduct[i] * rightProduct[n-(i+1)]
            productArr.append(res)
        return productArr