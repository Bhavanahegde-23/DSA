# Approach : Sliding window
# So here to keep count of characters use dict and check whether window size - max val is greater than k
# if (windowsize - max dict val) > k -- remove left most element or decrease the frequency and increment l
# same time keep track of the max len
# Time and space
# TC : O(n)
# SP : O(1) -- using dict it stores fixed char 26
from typing import DefaultDict
def longest_with_replacement(s , k):
    ans = 0
    d = DefaultDict(int)
    l = 0
    max_freq = 0
    for r in range(len(s)):
        d[s[r]] += 1
        max_freq = max(max_freq , d[s[r]])
        while (r-l+1)- max_freq > k :
            d[s[l]] -= 1
            if d[s[l]] == 0:
                del d[s[l]]
            l += 1
        ans = max(ans , r-l+1)
    return ans