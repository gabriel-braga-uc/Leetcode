class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_1 = 0
        index_2 = 1
        compensation = 0
        for x in nums:
            for y in nums[1::]:
                if x+y == target:
                    if index_1 == index_2:
                        index_2 += 1
                    if x+nums[index_2] == target:
                        return ([index_1, index_2])
                index_2 += 1
            index_1 += 1
            index_2 = 1