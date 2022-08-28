from collections import Counter
def longestPalindrome(s):
    freq = Counter(s)
    odd = False
    res = 0
    
    for k,v in freq.items():
        if v % 2 == 0:
            res += v
        else:
            res += v-1
            odd = True
    
    if odd:
        res += 1
        
    return res