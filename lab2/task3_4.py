def three_sum(nums):
    result = []
    n = len(nums)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i!=j and i!=k and j!=k and nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])

    return result
nums = [1,0,-1,5,-2,-3]
result = three_sum(nums)
print(result)
