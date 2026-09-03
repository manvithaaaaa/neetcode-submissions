class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num2=set()
        for i in nums:
            if i in num2:
                return True
            num2.add(i)
        return False