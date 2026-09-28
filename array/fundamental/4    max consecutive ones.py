''' Maximum Consecutive Ones

Subscribe to TUF+

Given a binary array nums, return the maximum number of consecutive 1s in the array.


A binary array is an array that contains only 0s and 1s.

Example 1

Input: nums = [1, 1, 0, 0, 1, 1, 1, 0]

Output: 3

Explanation:

The maximum consecutive 1s are present from index 4 to index 6, amounting to 3 1s

Example 2

Input: nums = [0, 0, 0, 0, 0, 0, 0, 0]

Output: 0
  '''
'''optimal'''
# def maxconones(arr):
#     n=len(arr)
#     count=0
#     maxcount=0
#     for i in range(0,n):
#         if arr[i]==1:
#             count+=1
#         else:
#             maxcount=max(maxcount,count)
#             count=0
#     return max(maxcount,count)
# n=int(input())
# arr=list(map(int,input().split()))
# print(maxconones(arr))
   


