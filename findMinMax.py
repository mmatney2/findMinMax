def findMinMax(nums):
    running_sum = 0
    while nums:
        max1 = max(nums)
        nums.pop(nums.index(max1))
        max2 = max(nums)
        nums.pop(nums.index(max2))
        running_sum += max2
    return running_sum
print(findMinMax([6,2,6,5,1,2]))

def optimumFind(nums):
    running_sum = 0
    nums.sort()
    for i in range(0, len(nums), 2):
        running_sum += nums[i]
    return running_sum

print(findMinMax([6,2,6,5,1,2]))

#given an array of distint integer and a value k, find all the pairs with a difference of k
#arr = [1,7,5,9,2,12,3]
#[(1,3),(5,7),(7,9),(3,5)]
def findPairs(arr, k):
    res = []
    for num in arr:
        if num + k in arr:
            res.append((num, num+k))
        # elif num - k in arr:
        #     res.append((num, num-k))
    return res
print(findPairs([1,7,5,9,2,12,3], 2))

