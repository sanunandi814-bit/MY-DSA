'''Union of two sorted arrays



Given two sorted arrays nums1 and nums2, return an array that contains the union of these two arrays. The elements in the union must be in ascending order.


The union of two arrays is an array where all values are distinct and are present in either the first array, the second array, or both.

Example 1

Input: nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 7]

Output: [1, 2, 3, 4, 5, 7]

Explanation:

The elements 1, 2 are common to both, 3, 4, 5 are from nums1 and 7 is from nums2

Example 2

Input: nums1 = [3, 4, 6, 7, 9, 9], nums2 = [1, 5, 7, 8, 8]

Output: [1, 3, 4, 5, 6, 7, 8, 9]

Explanation:

The element 7 is common to both, 3, 4, 6, 9 are from nums1 and 1, 5, 8 is from nums2'''

''' brute'''

# def mergearr(arr1,arr2):
#     set1=set(arr1)
#     set2=set(arr2)
#     st= set1 | set2            # | ye union ke liye use kiya gaya h
#     # st=set1.union(set2)      # essa bhi kar sakte h 
#     merge=sorted(st)
#     return merge
# n=int(input())
# m=int(input())
# arr1=list(map(int,input().split()))
# arr2=list(map(int,input().split()))
# print(mergearr(arr1,arr2))



''' optimal'''
# def mergearr(num1,num2):
#     n=len(num1)
#     m=len(num2)
#     res=[]
#     i,j=0,0
#     while i<len(num1):
#         if num1[i]<=num2[j]:
#             if not res or res[-1]!=num1[i]:
#                 res.append(num1[i])
#             i+=1
#         else:
#             if not res or res[-1]!=num2[j]:
#                 res.append(num2[j])
#             j+=1
#     while i<len(num1):
#         if not res or res[-1]!=num1[i]:
#             res.append(num1[i])
#         i+=1
#     while j<len(num2):
#         if not res or res[-1]!=num2[j]:
#             res.append(num2[j])
#         j+=1
#     return res
# n=int(input())
# m=int(input())
# num1=list(map(int,input().split()))
# num2=list(map(int,input().split()))
# print(mergearr(num1,num2))
