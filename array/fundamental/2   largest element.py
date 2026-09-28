'''Largest Element

Subscribe to TUF+

Given an array of integers nums, return the value of the largest element in the array

Example 1

Input: nums = [3, 3, 6, 1]

Output: 6

Explanation: The largest element in array is 6

Example 2

Input: nums = [3, 3, 0, 99, -40]

Output: 99

Explanation: The largest element in array is 99'''

'''brute'''
# def largestarr(arr):
#     n=len(arr)
#     arr.sort()
#     return arr[-1]
# n=int(input())
# arr=list(map(int,input().split()))
# print(largestarr(arr))

''' optimal'''
# def largestarr(arr):
#     n=len(arr)
#     largest=arr[0]
#     for i in  range(0,n):
#         if arr[i]>largest:
#             largest=arr[i]
#     return largest
# n=int(input())
# arr=list(map(int,input().split()))
# print(largestarr(arr))

''' or'''
# def largestarr(arr):
#     n=len(arr)
#     largest=float("-inf")           #yaha likhne ka style change
#     for i in  range(0,n):
#         largest=max(largest,arr[i]) # use of max func
#     return largest
# n=int(input())
# arr=list(map(int,input().split()))
# print(largestarr(arr))