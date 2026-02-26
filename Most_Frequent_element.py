def most_frequent(nums):
    freq = {}
    max_count = 0
    result = None
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
        if freq[num] > max_count:
            max_count = freq[num]
            result = num
    return result
nums = [1,1,2,3,2,4,2,7,7,7,7,7]
print(most_frequent(nums))