class Solution:
    def addElement(self, nums, x,pos):
        nums.append(0)
        for i in range(len(nums)-1, pos, -1):
            nums[i] = nums[i-1]
        nums[pos] = x
        return nums
nums = [10,20,30,40]
pos = 4
x = 25
obj = Solution()
print(obj.addElement(nums, x,pos))