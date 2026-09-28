'''Left Rotate Array by K Places

Subscribe to TUF+

Given an integer array nums and a non-negative integer k, rotate the array to the left by k steps.

Example 1

Input: nums = [1, 2, 3, 4, 5, 6], k = 2

Output: nums = [3, 4, 5, 6, 1, 2]

Explanation:

rotate 1 step to the left: [2, 3, 4, 5, 6, 1]

rotate 2 steps to the left: [3, 4, 5, 6, 1, 2]'''

''' LEFT'''

'''brute'''
# def leftrot(arr,k): # k me modification kiye isliye k lena pad
#     n=len(arr)
#     k=k%n   # ye rotations secure karne ke liye h
#     for _ in range(0,k):
#         first=arr.pop(0)
#         arr.insert(n,first)
#     return arr
# n=int(input())
# k=int(input())
# arr=list(map(int,input().split()))
# print(leftrot(arr,k))

''' OPTIMAL'''
# def rev(arr,l,r):
#     while l<r:
#             arr[l],arr[r]=arr[r],arr[l]
#             l+=1
#             r-=1
# def leftrot(arr,k):
#     n=len(arr)
#     k=k%n
#     rev(arr,0,k-1)
#     rev(arr,k,n-1)
#     rev(arr,0,n-1)
#     return arr
# n=int(input())
# k=int(input())
# arr=list(map(int,input().split()))
# print(leftrot(arr,k))

''' right
  arr=[1,2,3,4,5] k=2
  op= [4,5,1,2,3]'''

'''brute'''

# def rightrot(arr,k):
#     n=len(arr)
#     k=k%n
#     for _ in range(0,k):
#         first=arr.pop()
#         arr.insert(0,first)
#         return arr
# n=int(input())
# k=int(input())
# arr=list(map(int,input().split()))
# print(rightrot(arr,k))

'''optimal'''
# def rev(arr,l,r):
#     while l<r:
#         arr[l],arr[r]=arr[r],arr[l]
#         l+=1
#         r-=1
# def rightrot(arr,k):
#     n=len(arr)
#     k=k%n
#     rev(arr,n-k,n-1)
#     rev(arr,n-k-1,0)
#     rev(arr,0,n-1)
#     return  arr
# n=int(input())
# k=int(input())
# arr=list(map(int,input().split()))
# print(rightrot(arr,k))

''' per ye bhi lihk sakte h'''
# def rev(arr,l,r):
#     while l<r:
#         arr[l],arr[r]=arr[r],arr[l]
#         l+=1
#         r-=1
# def rightrot(arr,k):
#     n=len(arr)
#     k=k%n
#     rev(arr,0,n-1)
#     rev(arr,0,k-1)
#     rev(arr,k,n-1)
#     return  arr
# n=int(input())
# k=int(input())
# arr=list(map(int,input().split()))
# print(rightrot(arr,k))