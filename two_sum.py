'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.'''

'''
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
'''
class Solution:

    def twoSum(self, nums, target):
        to_yield_list = []
        for i,e in enumerate(nums):
            for i_1,e_1 in enumerate(nums):
                temp = e+e_1
                if i == i_1:
                    break
                if temp==target:
                    # print("temp:{}, e:{}, e_1:{}, i:{}, i_1:{}".format(temp,e,e_1,i,i_1))
                    to_yield_list.append(i)
                    to_yield_list.append(i_1)
                    return to_yield_list


sol = Solution()
print(sol.twoSum([2,7,11,15], 9))

'''Runtime: 4952 ms, faster than 11.72% of Python3 online submissions for Two Sum.
Memory Usage: 14.9 MB, less than 81.17% of Python3 online submissions for Two Sum.'''
