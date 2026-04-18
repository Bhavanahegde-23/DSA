# -Need to find the length of substring without duplicates
# -Approcah - 1
#     - Can use the set to store the char
#     - if find anything which is already in the set remove left one
#     - keep track of the length
#     - return length

## time and space
# TC: O(n)
# SC: O(n) -- in worst case but if charecters are fixed then it is O(1)
def longest_sub(s):
    maxLen = 0
    seen = set()
    l = 0
    for r in range(len(s)):
        while s[r] in seen:
            seen.remove(s[l])
            l += 1

        maxLen = max(maxLen , r-l+1)
        seen.add(s[r])

    return maxLen

## approach 2 using hashmap
## time and space
# TC: O(n)
# SC: O(n) -- in worst case but if charecters are fixed then it is O(1)
def long_substring(s):
    maxLen = 0
    l = 0
    map ={}

    for r in range(len(s)):
        if s[r] in map and map[s[r]] > l:
            l += map[s[r]] + 1

        map[s[r]] = r
        maxLen = max(maxLen , r-l+1)

    return maxLen
