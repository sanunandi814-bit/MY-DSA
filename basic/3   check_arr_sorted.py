''' check arr is sorted or not ( duplicate handle nhi karta)'''

'''Check if the Array is Sorted II

Subscribe to TUF+

Given an array nums of n integers, return true if the array nums is sorted in non-decreasing order or else false.

Example 1

Input : nums = [1, 2, 3, 4, 5]

Output : true

Explanation : For all i (1 <= i <= 4) it holds nums[i] <= nums[i+1], hence it is sorted and we return true.

Example 2

Input : nums = [1, 2, 1, 4, 5]

Output : false

Explanation : For i == 2 it does not hold nums[i] <= nums[i+1], hence it is not sorted and we return false.'''
# def sortarr(arr):
#     for i in range(0,n-1): # i+1 last tak jata h, to error dega but n-2 tak hi check karna hh
#         if arr[i]>arr[i+1]:
#             return False
#     return True
# n=int(input())
# arr=list(map(int,input().split()))
# print(sortarr(arr))

'''0r'''
# def sortarr(arr):
#     for i in range(1,n): # 1 se suru kiye h to n-1 tak le sakta h per n aacha ragega (becoz,arr[i]<arr[i-1], piche ja raha to error nhi dega)
#         if arr[i]<arr[i-1]: # essa bhi likh sakte h
#             return False
#     return True
# n=int(input())
# arr=list(map(int,input().split()))
# print(sortarr(arr))

