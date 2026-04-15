#
#
# def targetSum(nums , target):
#     seen ={}
#     for i in range(len(nums)):
#         s = target - nums[i]
#         if s in seen:
#             return [seen[s] , i]
#         seen[nums[i]] = i
#
#
# nums = [2,7,11,15 ,7]
# target = 14
# print(targetSum(nums , target))
#
#
# # You are given a binary array nums containing only 0s and 1s, and an integer k. You can flip at most k zeros to ones. Your task is to find the maximum number of consecutive 1s you can get in the array after performing at most k flips.
# # nums = [1,1,0,0,1,1,0,1,1,1] k = 2
#
# def maxlen(nums , k):
#     left  = 0
#     maxlen = 0
#     for i in range(len(nums)):


def addFunc(func):
    def wrapper(*args):
        print("hii")
        a = func(*args)
        print("bye")
        return a
    return wrapper


@addFunc
def func1():
    print("abc")

@addFunc
def add(a,b):
    return a+b

print(add(3,4))









