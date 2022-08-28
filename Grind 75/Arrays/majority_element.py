
def majorityElement(nums):
    ele = nums[0]
    count = 1
    for i in range(1,len(nums)):
        if ele == nums[i]:
            count+=1
        else:
            count-=1
        if count == 0:
            ele = nums[i]
            count = 1
    return ele


# Approach1: Brute-force approach: For two loops, one inside another for every element
#            take the count and check whther that is greater than n/2    
# Approach2: use hashmap: t(n) - O(n), s(n) - O(n)
# Approach3: Moore's Voting algorithm