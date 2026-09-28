'''remove dupliacte from sorted( in place, means arr me hi change karna h)'''
'''Remove duplicates from sorted array

Subscribe to TUF+

Given an integer array nums sorted in non-decreasing order, remove all duplicates in-place so that each unique element appears only once.

Return the number of unique elements in the array.

If the number of unique elements be k, then,

Change the array nums such that the first k elements of nums contain the unique values in the order that they were present originally.  
The remaining elements, as well as the size of the array does not matter in terms of correctness.  
The driver code will assess correctness by printing and checking only the first k elements of the modified array.

An array sorted in non-decreasing order is an array where every element to the right of an element is either equal to or greater in value than that element.

Example 1

Input: nums = [0, 0, 3, 3, 5, 6]

Output: 4

Explanation:

Resulting array = [0, 3, 5, 6, _, _]

There are 4 distinct elements in nums and the elements marked as _ can have any value.

Example 2

Input: nums = [-2, 2, 4, 4, 4, 4, 5, 5]

Output: 4

Explanation:

Resulting array = [-2, 2, 4, 5, _, _, _, _]

There are 4 distinct elements in nums and the elements marked as _ can have any value'''

# def dupsort(arr):
#     n=len(arr)
#     freqmap={}
#     for i in  range(0,n):
#         freqmap[arr[i]]=0 # value me kuch bhi le sakta hu ( bas keys qnique ke liye dict liye)
#     j=0
#     for k in freqmap:
#         arr[i]=k
#         j+=1
#     return j+1 # kitne duplicate h dega
# n=int(input())
# arr=list(map(int,input().split()))
# print(dupsort(arr))

''' optimal'''
# def dupsort(arr):
#     n=len(arr)
#     i=0
#     j=i+1
#     if n==1:  # ye ek element ka edge case h
#         return 1
#     if not arr:
#       return 0
#     while j<n:
#         if arr[j]!=arr[i]:
#             i+=1
#             arr[i],arr[j]=arr[j],arr[i]
#         j+=1
#     return i+1
# n=int(input())
# arr=list(map(int,input().split()))
# print(dupsort(arr))

''' method2(brute)'''
# def dupsort(arr):
#     n=len(arr)
#     seen=set()
#     idx=0
#     for num in arr:
#         if num not in seen: # ye arr ko yaad rakhta h
#             seen.add(num)
#             arr[idx]=num # ye arr ko overweite katra h
#             idx+=1
#     return idx

# n=int(input())
# arr=list(map(int,input().split()))
# k=dupsort(arr)
# print(k)
# print(arr[:k]) # ye new arr ko dikhane ka tarika h
