'''
Two Sum (Unsorted Array Version)

Problem Statement :- 
Given an unsorted integer array nums and an integer target, return indices of the two numbers 
such that: nums[i] + nums[j] = target

Conditions:
1. Each input has exactly one solution
2. You cannot use the same element twice
3. Return indices, not values

Example :-
Input: nums = [2, 7, 11, 15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9

'''

# Brute Force Approach
''' Check every possible pair using two loops

Algorithm :-
1. Start loop i from 0 to n-1
2. Start loop j from i+1 to n-1
3. If nums[i] + nums[j] == target → return [i, j]

'''
'''

class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i,j]
nums = [2,7,11,15]
target = 9
obj = Solution()
print(obj.twoSum(nums,target))

# TC :- O(n*n), SC :- O(1)

'''

# Optimal Solution

'''
Instead of checking all pairs:
1. For each element, calculate: complement = target - nums[i]
2. Check if complement already exists in a dictionary
3. If yes → return indices
4. Else → store current number with its index
'''

class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i
        return []
nums = [2,7,11,15]
target = 9
obj = Solution()
print(obj.twoSum(nums,target))

'''TC :- O(1), SC :- O(n)'''