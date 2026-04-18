# #Aproach
# - Its sliding window as we got defined window size
# - Keep track of current sum and max sum , and keep sliding if the window size more than k then remove left element ,
# if window size equal then update maxsum

def max_sum_k(arr , k):
    maxSum = 0
    sum = 0
    l = 0
    for r in range(len(arr)):
        sum += arr[r]

        if (r-l+1)>k:
            sum -= arr[l]
            l += 1

        if (r-l+1) == k:
            maxSum = max(maxSum , sum)

    return maxSum

arr = [2,1,5,1,3,2]
k=3
print(max_sum_k(arr,k))