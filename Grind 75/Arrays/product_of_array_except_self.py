def productExceptSelf(nums):
    ans = [0]*len(nums)
    ans[0] = 1
    for i in range(1,len(nums)):
        ans[i] = ans[i-1] *nums[i-1]
    r = 1
    for i in range(len(nums)-1,-1,-1):
        ans[i] = r*ans[i]
        r*=nums[i]
    return ans

# Approach1: Take left array and right array and then make a product of both
# Approach2: Take only 1 array and take left product, right product would be counted in a fly.