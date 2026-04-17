## Sliding window problems Mainly 2 types
1.Fixed size window
- window size will be fixed
- Example : Max sum subarray of size k
- code snippet

###############################################
    l = 0
    window_sum = 0
    ans = 0
    
    for r in range(len(arr)):
        window_sum += arr[r]
    
        if r - l + 1 > k:
            window_sum -= arr[l]
            l += 1
    
        if r - l + 1 == k:
            ans = max(ans, window_sum)
    
    return ans
###############################################

2.Variable size window
- Window expands and shrinks based on condition
- Example : Longest substring without repeating characters or Minimum window substring
- code snippet

################################################
    l = 0
    ans = 0
    
    for r in range(len(arr)):
        # expand window
    
        while invalid_condition:
            l += 1   # shrink window
    
        ans = max(ans, r - l + 1)

##################################################

