'''
✅ Two Sum II - Input Array Is Sorted
📌 Pattern Name
🟢 Two Pointer Pattern (Opposite Direction Pointers)

Used when:
Array is sorted
Need to find pair with given sum
Want better than O(n²)

📌 Problem Statement
Given a sorted array (ascending order) of integers numbers and an integer target,
return the indices (1-based indexing) of the two numbers such that: numbers[i] + numbers[j] = target

Conditions:
1. Exactly one solution
2. Cannot use same element twice
3. Return indices in 1-based indexing

📥 Example
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]

'''

# Brute Force Approach
'''Check every possible pair.'''

'''class Solution:
    def twoSum(self,numbers, target):
        n = len(numbers)
        for i in range(n):
            for j in range(i + 1, n):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
numbers = [2,7,11,15]
target = 9
obj = Solution()
print(obj.twoSum(numbers,target))

# TC :- O(n*n), SC :- O(1)
'''

# Optimal Solution
'''
Since array is sorted:
1. If sum is too small → move left pointer right
2. If sum is too large → move right pointer left
This eliminates unnecessary comparisons.
'''

class Solution:
    def twoSum(self,numbers, target):
        left = 0
        right = len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []
numbers = [2,7,11,15]
target = 26
obj = Solution()
print(obj.twoSum(numbers,target))

'''TC :- O(n), SC :- O(1)'''