# n=int(input("enter a any number:"))
# i=1
# while i<=n:
#     print(n,"*",i,"=",n*i)
#     i=i+1
# # n=int(input("enyter a number:"))
# s=0
# i=2
# while i<=n:
#     s=s+i
#     i=i+1
#
# print(s)

#
# n=int(input("enyter a number:"))
#
# i=1
# while i%2 in n:
#     print(i)
#     i=i+1

# # print()
# x=range(1,10)
# if x%2==0:
#     print(x)



# even numbers
# i=0
# n=range(1,11)
# for i in n:
#     if i%2==0:
#        print(i)
#
#facter sum of the value

#
# n=4
# s=0
# for i in range(1,n+1):
#     if n%i==0:
#         # i=i+1
#         s=s+i
#         print(i)
# print('sum of the values:',s)



# # table
# a=int(input("enter any number"))
# for i in range(1,11):
#     print(a,"*",i,"=",a*i)
# n=4
# i=1
# for i in range(1,10):
#     if n%i==0:
#         print(i)
#         i=i+1
#         print(i)
import time
#
# for u in range(1,3):
#    for o in range(3, 0, -1):
#       for i in range(1, 5):
#          # slee.time(.3)
#          print(i, end="")
#       print('*')
#    print("*")



# n=3
# for j in range(0,n+1):
#  for i in range(1,j+1):
#     # i=i+1
#     print("*",end="")
#
#        print("*")
#  print("")

# 1)

# n=int(input("enter any numer:"))
# for i in range(1,n+1):
#    for j in range(1,i+1):
#       print(j,end="")
#    print(" ")

# out:
# 1
# 12
# 123
# 1234

# 2)

#    n = int(input("enter any numer:"))
#    for i in range(1, n + 1):
#       for j in range(1, i + 1):
#          print("*", end="")
#       print(" ")
#
# out:*
# **
# ***
# ****
# *****
#
#
#
#3)
# n=int(input("eny:"))
# for i in range(n,0,-1):
#    for j in range(i,0,-1):
#       print(i,end="")
#
#
#    print("")
#
# n = int(input("enter any numer:"))
# for i in range(1,n+1):
#    for j in range(1,n+1):
#       print(i ,end="")
#
#       # print(j,end='')
#    print(" ")

#
# out:1111
# 2222
# 3333
# 4444
#
# n=4
# for i in range(n):
#    # for j in range(i+1):
#    #    print('',end="")
#    for j in range(i,n):
#       i=i+1
#       print(i,end="")
#    print()
#
# out:
# 1234
# 234
# 34
# 4


#
# n=3
#
# b=0
# for i in range(1,n+1):
#    for j in range(1,n+1):
#        b=b+1
#        print(b,end='')
#    print('')

# 123
# 456
# 789
# n=6
# i=1
# while i<n:
#     if i==5:
#       break
#     i=i+1
#     print(i)
# n=int(input("enter any number"))
# i=1
# while i<10:
#     i=i+1
#     print(n,"x",i,"=",n*i)
# import time
# import random
# for i in range(1,10):
#     pr=random.randint(111,999)
#     print(pr)
#
# x=[10,20,30,40]
# index=0
# while index<4:
#     print(index)
#     index=index+1

# s="welcome"
# print(s[1:7:])
#
# print(s[1:7:])
# print(s[-1:7:])
# print(s[:7:-1])
# print(s[1:7:])
# s1=[0:3:]
# s2=[-1:-7:1]
# print(s1+s2)

# s=int(input())
# s2=" "
# l=len(s)-1
# while l>=0:
# #     s2=s2+s[l]
# #     l=1-1
# # print(l)
# x=[1,32,4,2,213,1,3,2,34,4]
# print(list(sorted(x)))
# print(list(sorted(x,reverse=True)))
# print(len(sorted(x)))

s="anji is a \"nice\" sessan"
print(s)

s='anji is a "nice" sessan'
print(s)

