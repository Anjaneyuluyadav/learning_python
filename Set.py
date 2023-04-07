# set predefind class the class set()
# insertion is not mainten
# douplicact are not allowed



# set=set()
# print(type(set))
# #
# # s1={12,2,3,4}
# # s2={""}
# # s3=s2.add(s1)
# # print(s3)
# s1={1,2,3}
# s2={2,3,4}
# s1.update(s2)
# print(s1)

#
# def check_prime(n):
#     c=0
#     for i in range(1,n+1):
#         if n%i==0:
#             c=c+1
#     if c==2:
#         return n
#
# Prime_list=[2]
# Pal_List=[]
#
#
#
# f={12,3,4,0,"anji",5,9,7,88,7}
# b=any(f)
# print(type(b))

# def myfun(x,y):
#     print("a val:",x)
#     print(y)
#
# myfun(2,4)
# # myfun(x=7,y=9)
# # myfun(x=5,y=9)
# myfun(5,y=8)


#
# def myfun(*x,**y):
#     print("hi")
#     len=len(*x)
#     for i in len:
#         print("sum",i)
#     print("")
# myfun(10,23,2,44,32,2,32,neme="anji",name="ufj")
# outt=myfun(124,432342,name="anji")
# # print(outt)


#1)
# def myfun(name):
#     print("hi",name,"hava a nice day")
# def Dfun(fu):
#  def warri(x):
#    if x=="nari":
#        print("hi",x,"good day")
#    else:
#         myfun(x)
#  return warri
# inn=Dfun(myfun)
# inn("nari")


# def greet(name):
#     print("hi",name,"nice day")


#2)
# def Dgreeting(func):
#     def wraper(name):
#         if name=="anji":
#             print("hi",name,"good day")
#         else:
#             greet(name)
#     return wraper
# @Dgreeting
# def greet(name):
#     print("hi",name,"nice day")
# # inn=Dgreeting(greet)
# greet("anji")


# x='Hell38#%%&&&8@@@kj98'
# y=list(x)
# out=[]
# for i in range(len(y)):
#     if x[i].isalpha():
#         out.append(x[i])
#     elif x[i].isnumeric():
#         out.append(x[i])
#     else:
#         if x[i]not in out:
#             out.append(x[i])
# print(str(out))

# x="10,3,3,5,6,7,8,3,jjfn","gu"
# out=[]
# for i in range(len(x)):
#     if x[i].isalpha():
#         out.append(x[i])
#     else:
#         if x[i] not in out:
#             out.append(x[i])
# d=(out)
# print(d)




# Strings :
# # 1)Reverse the  words in given string
# x="anji"
# v=list(x)
# b=v[::-1]
# print(type(b))
# n=str(b)
# print(n)
# for i in range(len(v)):
#
#     n=x[i]
#     print(n,end="")


# Input: s = “i love programming very much” 
# Output: s = “much very programming love i” 
# Hint : first reverse the string next reverse the each word in given string
# 2) Input: X = "25", Y = "23" Output: 48 Explanation: The sum of 25 and 23 is 48.
# 3) x= print the longest palindrome strings from given string
# X=' amma my madam is good'
# Output : logenest palindrome is madam
# 4) remove all duplicates from given string
# X='ABCDEAFGD'. Output : ABCDEFG remove all duplicates
# 5) count the charters of given string
#  X ='ABCDAEBC
# Output :
# A ->2
# B->2
# C->2
# D ->1
# E->1
# 6) find the length of each word and print in dict
#  X= " python is good"
# Output : {'python' :5 ,'is' :2,'good':4}
# 7) x='ABCD' print the index of each char and make it as dict
#     Output: {'a':0,'b':1,'c':2,'d':3}
# 8) x=[['hi,'helo'],['how', 'are', 'you']]
# Output: hi hello how are you
# 9) x='abAB12$&d' count all uppercase , Lowercase, numbers, special chars from strings
# 10.x='abAB1121$&d remove all charecters except number's 
# Output : 1121
# x=10
# def myfun():
#     def nyfun():
#         global x
#         x=x+20
#         d=globals()
#         print(d.get('x'))
#
#     nyfun()
# myfun()
# lst=[2,5,7]
# for i in lst:
# #     if
# def mj(x,c,b):
#     if x>c:
#         print("result:",x)
#     elif c>b:
#         print("result:",c)
#     else:
#         if x>b:
#           print("result",b)
#
# mj(2,4,8)
#
# x=lambda a,b:a+b
# n=x(2,3)
# print(n)


# li=[2,3,4]
# x=list(map(lambda sq:sq*sq,li))
# print(x)


# j=lambda a,b: a if a>b else b
# k=j(5,7)
# print(k)


#
# x=lambda a,b:max(a,b)
# a=20
# b=43
#
# n=x(a,b)
# print(n)



import time
print(help(time.sleep()))