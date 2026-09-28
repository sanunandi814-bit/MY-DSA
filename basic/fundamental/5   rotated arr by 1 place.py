'''rotated arr right by onr place'''
''' arr=[1,2,3,4,5,6]
    op=arr=[6,1,2,3,4,5]'''
# LAST ELEMENT IN THE FIRST PLACE AND OTHER SHIFTED RIGHT
'''brute'''
# def rotrightby1(arr):
#     n=len(arr)
#     arr[:]=[arr[-1]]+arr[0:n-1]  # ye kiye becoz signle no list kke sth nhi judta
#     # arr[:]=[arr[n-1]]+arr[0,n-1] ye bhhi likh sakte h
#     return arr #  arr[:] ye original arr me change karega (n-2 tak hi chalega)
# n=int(input())
# arr=list(map(int,input().split()))
# print(rotrightby1(arr))

''' optimal'''
# def rotrightby1(arr):
#     n=len(arr)
#     temp=arr[n-1]
#     for i in range(n-2,-1,-1):
#         arr[i+1]=arr[i]
#     arr[0]=temp
#     return arr
# n=int(input())
# arr=list(map(int,input().split()))
# print(rotrightby1(arr))

'''rotate arr left by one'''
'''arr=[1,2,3,4,5,6]
   op=arr=[2,3,4,5,6,1]'''
# def rotleftby1(arr):
#     temp=arr[0]
#     for i in range(1,n):
#         arr[i-1]=arr[i]
#     arr[n-1]=temp
#     return arr
# n=int(input())
# arr=list(map(int,input().split()))
# print(rotleftby1(arr))


'''brute ( approach by left)'''
# a=[1,2,3,4,5,6]
# n=len(a)
# print(a[1:n+1]+[a[0]])
