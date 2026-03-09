class Solution:
    def bubble_sort(self, arr):
        n = len(arr)

        for i in range(n):
            swapped = False

            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True

            if not swapped:
                break

        return arr
arr = [1,4,3,7,8]
obj = Solution()
print(obj.bubble_sort(arr))