''' second largest'''
'''brute'''

# def secondarr(arr):
#     n=len(arr)
#     arr.sort()
#     return arr[-2]
# n=int(input())
# arr=list(map(int,input().split()))
# print(secondarr(arr))

''' ager [8,8,7,6,5] hua to [5,6,8,8] ; kon sa second largest
hoga nhi bata isliye
EK SET ME SORT KARTE H JO DUPLICATE REMOVE KAREGA
AUR AGER LEN( SET KA) 2 SE KAM HOGA TO DUPLICATE BATEGA'''

# def secondarr(arr):
#     n=len(arr)
#     val=sorted(set(arr))
#     if len(val)<2:
#         return -1
#     return val[-2]
# n=int(input())
# arr=list(map(int,input().split()))
# print(secondarr(arr))

''' optimal ( duplicate ko handle nhi karta)'''
# def secondarr(arr):
#     n=len(arr)
#     lar=float("-inf")
#     seclar=float("-inf")
#     for i in range(0,n):
#         if arr[i]>lar:
#             seclar=lar
#             lar=arr[i]
#         elif arr[i]>seclar and arr[i]!=lar:
#             seclar=arr[i]
#     return seclar
# n=int(input())
# arr=list(map(int,input().split()))
# print(secondarr(arr))

'''Second Largest Element

Subscribe to TUF+

Given an array of integers nums, return the second-largest element in the array. If the second-largest element does not exist, return -1.

Example 1

Input: nums = [8, 8, 7, 6, 5]

Output: 7

Explanation:

The largest value in nums is 8, the second largest is 7

Example 2

Input: nums = [10, 10, 10, 10, 10]

Output: -1

Explanation:

The only value in nums is 10, so there is no second largest value, thus -1 is returned

'''
''' optimal( duplicate ko handle kaerega)'''
# def secondarr(arr):
#     n=len(arr)
#     if n<2:
#         return -1    # ek hi element rahega to -1 return karega
#     lar=float("-inf")
#     seclar=float("-inf")
#     for i in range(0,n):
#         if arr[i]>lar:
#             seclar=lar
#             lar=arr[i]
#         elif arr[i]>seclar and arr[i]!=lar:
#             seclar=arr[i]
#     return seclar if seclar !=float("-inf") else -1 # duplicate hatane ke liye warna -inf hojayega
# n=int(input())
# arr=list(map(int,input().split()))
# print(secondarr(arr))