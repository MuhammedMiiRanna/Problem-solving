class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = [None, None]
        length = len(nums)
        results = {}
        for index in range(length):
            if target - nums[index] in results:
                return [nums.index(target - nums[index]),
                        nums.index(nums[index], nums.index(target - nums[index]) + 1)]
            else:
                results[nums[index]] = nums[index]
        return result


# nums, target, expected
samples = [
    [[2, 7, 11, 15], 9, [0, 1]],
    [[3, 2, 4], 6, [1, 2]],
    [[3, 3], 6, [0, 1]],
    [[-1, -2, -3, -4, -5], -8, [2, 4]],
    [[-3, 4, 3, 90], 0, [0, 2]]
]
samples = samples[:]
print(samples)
solution = Solution()
for sample in samples:
    result = solution.twoSum(sample[0], sample[1])
    print('>> Expected result:', sample[2])
    print('>> result:', result)
    print('*'*25)


# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         nums, target = list(map(abs, nums)), abs(target)
#         numbs = sorted(nums)
#         result = [None, None]
#         length = len(numbs)
#         for index_1 in range(length-1):
#             for index_2 in range(index_1+1, length):
#                 if numbs[index_1] + numbs[index_2] == target:
#                     result = [nums.index(numbs[index_1]),
#                               nums.index(numbs[index_2], nums.index(numbs[index_1])+1)]
#                 elif nums[index_1] + nums[index_2] > target:
#                     break
#         return result


# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         result = [None, None]
#         length = len(nums)
#         for index_1 in range(length-1):
#             for index_2 in range(index_1+1, length):
#                 if nums[index_1] + nums[index_2] == target:
#                     result = [index_1,
#                               index_2]
#                     break
#         return result
