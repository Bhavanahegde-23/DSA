# Approach : Sliding window
# keep track of char frequency using dict
# check ( number of zeros ) > k if yes decrement left element freq and increment l
# Time and space
# TC : O(n)
# SP : O(1) -- using dict it stores fixed char 26
from typing import DefaultDict
def max_consecutive_ones(arr , k):
    ans = -1
    l = 0
    d = DefaultDict(int)
    zero = 0
    for r in range(len(arr)):
        d[arr[r]] += 1
        zero = d[0]
        while zero > k :
            d[arr[l]] -= 1
            l += 1

        ans = max(ans,r-l+1)

    return ans