
# import sys
# x=int(sys.argv[1])
# y=int(sys.argv[2])
# s=x+y
# print("type of :",type(s))
# print("type of :",s)
# # print("type of sum:",sum(x,y))  #type /E


import random
from operator import index as _index

for i in range(1,11):
    print(random.randint(6,9),random.randint(11,99),chr(random.randint(97,122)),random.randint(1,9),chr(random.randint(65,90)))