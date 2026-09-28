'''
Move Zeros to End

Subscribe to TUF+

Given an integer array nums, move all the 0's to the end of the array. The relative order of the other elements must remain the same.


This must be done in place, without making a copy of the array.

Example 1

Input: nums = [0, 1, 4, 0, 5, 2]

Output: [1, 4, 5, 2, 0, 0]

Explanation:

Both the zeroes are moved to the end and the order of the other elements stay the same

Example 2

Input: nums = [0, 0, 0, 1, 3, -2]

Output: [1, 3, -2, 0, 0, 0]'''

''' brute'''
# def zeroend(arr):
#     n=len(arr)
#     temp=[]
#     for i in range(0,n):
#         if arr[i]!=0:
#             temp.append(arr[i])
#     templen=len(temp)
#     for i in range(0,templen):
#         arr[i]=temp[i]
#     for i in range(templen,n):
#         arr[i]=0
#     return arr
# n=int(input())
# arr=list(map(int,input().split()))
# print(zeroend(arr))

''' optimal'''
# def zeroend(arr):
#     n=len(arr)
#     if n==1:   # edge  case ek element ke liye
#         return
#     i=0
#     while i<n:
#         if arr[i]==0:
#             break
#         i+=1
#     if i==n:  # edge case ager input/qno me zero na ho to none return hoga (eg,1 2 3 4 5     -> none)
#         return
#     j=i+1
#     while j<n:
#         if arr[j]!=0:
#             arr[i],arr[j]=arr[j],arr[i]
#             i+=1
#         j+=1
#     return arr
# n=int(input())
# arr=list(map(int,input().split()))
# print(zeroend(arr))

''' optimal(for loop)'''
# def zeroend(arr):
#     n=len(arr)
#     i=0
#     for j in range(0,n):
#         if arr[j]!=0:
#             arr[i],arr[j]=arr[j],arr[i]
#             i+=1
#     return arr
# n=int(input())
# arr=list(map(int,input().split()))
# print(zeroend(arr))
