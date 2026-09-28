'''Find missing number



Given an integer array of size n containing distinct values in the range from 0 to n (inclusive), return the only number missing from the array within this range.

Example 1

Input: nums = [0, 2, 3, 1, 4]

Output: 5

Explanation:

nums contains 0, 1, 2, 3, 4 thus leaving 5 as the only missing number in the range [0, 5]

Example 2

Input: nums = [0, 1, 2, 4, 5, 6]

Output: 3

Explanation:

nums contains 0, 1, 2, 4, 5, 6 thus leaving 3 as the only missing number in the range [0, 6]'''

''' brute(tc-> o(n2) , sc-> o(1))'''
# def missingarr(arr):
#     n=len(arr)
#     for i in range(0,n+1):
#         if i not in arr:
#             return i
# n= int(input())
# arr=list(map(int,input().split()))
# print(missingarr(arr))

''' brute( o(n))'''
# def missingarr(arr):
#     n=len(arr)
#     freq={}
#     for i in range(0,n+1):  # ''' dic banya 1 se n+1 tak dalna and sabka val=0
#         freq[i]=0
#     for i in arr:           # ''' arr me se val ko update karna
#         freq[i]+=1
#     for k,v in freq.items():#''' dict me k,v ko lena and k ko return karna
#         if v==0:
#             return k
# n= int(input())
# arr=list(map(int,input().split()))
# print(missingarr(arr))


''' optimal  ( O(n),O(1))'''
# def missingarr(arr):
#     n=len(arr)
#     total=0
#     for i in range(0,n+1):
#         total+=i
#     return total-sum(arr)
# n= int(input())
# arr=list(map(int,input().split()))
# print(missingarr(arr))




