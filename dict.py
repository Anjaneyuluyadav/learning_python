# how to inserct the value
# d={}
# print(type(d) )
# d["a"]=10
# d[10]="anji"
# print(d)


# how to updata value
# d={"sno":10,"sname":'anji'}
# a,b=d
# print("result:",a,b)
#
# for i in d:
#     print((i))

# dict : is a collection of key and val pair
# if we want to represets - group of objects a s keys  value pairs then  we should go for dict
# syntax : varname={key:val,key:val ..........n}
# duplicte keys r not allowed but values can be duplicated
# hetriginious objects r allowed(key and val can be any data type)
# dict is mutable (we can changge the vbal for perticuler keys)
# index and slicing are not appliavlable
# dic is dynamic (we can add n no of elements)

# how to access dic elements
# x={'A':10,10:'B',5.0:'hello'}
# print(x[10])
# print(x[5.0])
# print(x['A'])
# how to chnge value in dict

# x={'A':100,'B':200,'C':300}
# x['A']=900
# print(x)
# x['C']=1000
# print(x)

# x={'A':100,'B':200,'C':300,'A':300}
# print(x)

# how to define the dict
# x=dict()
# print(type(x))
# x={}
# print(type(x))
# del -> uswd for delete the elemnts in iteratble object(set,list,tuple,strings)
# del used for to delete perticuler key and val if key is exits if key is not exits it will throw the key error
# x={'A':100,'B':200,'C':300}
# del x['D']
# print(x)

# x=[10,20,30,40,50]
# del x[2]
# print(x)
# a=10
# a=a+10
# print(a)

# clear -> used to remove the all the key and val pair in dict
# x={'A':100,'B':200,'C':300,'A':300}
# #x.clear() #x={}
# x={}
# print(x)

# len
x = {'A': 100, 'B': 200, 'C': 300, 'A': 300}
# print(len(x))
# print(x['C'])
# get -> used to get the value from the dict using key
# print(x.get('A')) # x['A']
# print(x.get('B'))  # x['B']
# pop -> pop used for to remove the perticuler key and val pair
# x.pop('A')
# print(x)
# del x['C']
# print(x)
# popitem : it removes the key and val pair from the last and it will return the (key ,val) pair
# x={'A':100,'B':200,'C':300,'A':300}
# x.popitem()
# print(x)
#
# x={'A':100,'B':200,'C':300}
# x.popitem()
# print(x)
# x.popitem()
# print(x.popitem())
# x.popitem()
# print(x.popitem())#key error
# keys ->keys fun used to get only keys in list format
x = {'A': 100, 'B': 200, 'C': 300}
# keys=list(x.keys())
# print(keys)
# values() -> values fun to get only values in list format
# val=list(x.values())
# print(val)

# items() -> it returns the list of tuples (key and value pair)
# print(x.items())
# key_val=list(x.items())
# print(key_val)

# copy -> used to copy the one dict to anoter dict
x = {'A': 100, 'B': 200, 'C': 300}
# y=x
# y=x.copy()
# print(type(y))
# print(x)
# setdefault -> having two agrs one is key another one is val
# if key is already exits it will return the perticuler value associated with that key
# if key is not exits its goingg to add in dict with defaulr val (None)
# x.setdefault('D',300)
# print(x)
# x.setdefault('E',)
# print(x)
# print(x.setdefault('B',1000))
# x.setdefault('B')
# print(x)
# print(x.setdefault('A'))
# print(x.setdefault('C'))
# x.get('A')
# print('B')
# print()
# x={'A':100,'B':200,'C':300}
#
# x.setdefault('D')
# print(x)
# print(x.setdefault('D',1000))

# x.setdefault('D','ABCD')
# print(x)
# x.setdefault('E')
# print(x)
# print(x.setdefault('B'))
# print(x.setdefault('E',5000))
# update -> used to update te dict with anothe dixt
# if key is already xits it updatin only te val if key is not exits it will updte key and value both
# x={'A':100,'B':200,'C':300}
# y={'E':300,'F':500}
# x.update(y)
# #
# print(x)
# y.update({'A':4,'B':600})
# print(y)
# print(x)

# x={'A':10,'B':20}
# y={'C':400}
# x.update(y)
# print(x)
# y.update({'a':4,'b':50})
# print(y)

# x={'A':10,'B':20}
# y={'A':200,'C':500}    #{'A':10,'B':20 ,'A':200,'C':500}
# x.update(y)
# print(x)

# fromkeys: used to create new dict
# we can assin common val for the all the keys in  dict

# x=[1,2,3]
# val=100
# val=[100,200]
# out={}
# out=out.fromkeys(x,val)
#
# print(out)

# nested dic : dic inside the is called nested dict
# x={'A':{1,2,3},'B':[3,4,5],'C':{'x':100,'y':200}}
# print(x['B'])
# print(x.get('B'))
# print(x['B'][2])
# print(x.get('B')[2])
# print(x['C']['y'])
# print(x.get('C')['y'])

# swap a keys and values in dict

# # zip : zip fun used to combine two iterable objects
# x=[1,2,3]
# y=[4,5,6]
# out=list(zip(x,y))
# print(out)

# x={'A':100,'B':200} # {100:'A',200:'B'}
# key=list(x.keys())
# val=list(x.values())
# out=dict(zip(val,key))
# print(out)

# logic 2

# x={'A':100,'B':200}
#
# keys=list(x.keys()) # [A,B]
# val=list(x.values()) #[100,200]

# out={}
# for i in range(len(keys)):   #{100:'A',200:'B'}
#     out[val[i]]=keys[i]
# print(out)

# out=x.fromkeys(val)   # [100:None,200:None]
# c=0
# for key,val in out.items():
#     out[key]=keys[c]
#     c=c+1
# print(out)
x = {'A': 100, 'B': 200}
# keys=list(x.keys()) # [A,B]
# val=list(x.values()) #[100,200]
# out={}
# for val,key in x.items():
#     out.setdefault(key,val)
# print(out)

# x="ABCABCDE"  # {'A':2,'B':2,'C':2,'D':1,'E':1}
# y=list(x)
# print(y)
# out=[]
# [out.append(i) for i in y if i not in out]
# print(out)  # ['A', 'B', 'C', 'D', 'E']
# finalout={}
# for i in range(len(out)):
#     finalout[out[i]]=x.count(out[i])
# print(finalout)

# x={'A':{'x':200,'y':1000},'B':[3,4,5],'C':{'x':100,'y':200}}
# x.pop('B')
# print(x)
# key=list(x.keys()) #['A','B','C']
# print(key)
# val=list(x.values())  # [{'x': 200, 'y': 1000}, [3, 4, 5], {'x': 10000, 'y': 20000}],
# print(val)
# #print(val)
# out={}
# for i in range(len(keys)+1):
#     if type(val[i])==list:
#         print("HI")
#     else:
#        out.setdefault(key[i],val[i])
#
# print(out)
# !) create a dict called student  with student name and marks

# {"ST!_NAME":"KAMAL","ST1_MARKS":300,ST2_NAME:"ANJI","ST2_MMARKS":300}
# {"KAMAL":200,"ANJI":500}
# n=int(input("Enter the student count :"))    # 3
# student={}
# while(n>=1):
#     name = input("Enter Student name :")
#     marks = int(input("Enter student marks :"))
#     student[name]=marks
#     n=n-1
# print("Student dict :",student)

# x={'A':10,'B':20}  # {'A':100,'B':400}
# keys=list(x.keys())
# vals=list(x.values())
# vals=[pow(i,2) for i in vals]
# print(keys)
# print(vals)
# out={}
# out=dict(zip(keys,vals))
# print(out)

# dict comphrehension : the operation which we r doing inside the dict is called dict comphregension
# we can create new dict using dict comphrehension
# syntx ={Expression for i,j in dict if con
# x={'A':10,'B':20}
# # print(x.items())
# # for i,j in x.items():
# #     print(i,end=' ')
# #     print("key :",i,"val :",j)
# out={i:pow(j,2) for i,j in x.items()}     #{'A': 100, 'B': 400}
# print(out)
# out={i:pow(j,3) for i,j in x.items()}      #{'A': 1000, 'B': 8000}
# print(out)
# x={'A':10,'B':20}
# out={i:x[i]*10 for i in x.keys()}
# print(out)
# x='java is good' # {"python":5,'is':2,"good":4}
# keys=x.split()
#
# val=[]
# for i in keys:  # ['python', 'is', 'good']
#     val.append(len(i))
# print("keys",keys)
# print("val :",val)
#
# out=dict(zip(keys,val))
# print(out)
# keys ['java', 'is', 'good']
# val : [4, 2, 4]

# out={}
# for i in range(len(keys)):
#     out[keys[i]]=val[i]
# print(out)

# x={'1':['a','b'],'2':['c','d']}  # ['ac','ad','bc','bd']
#
# val=list(x.values())
# print(val)
# ouput=[]     0   1
# a=val[0] # ['a','b']
# b=val[1] # ['c', 'd']
#          #  0     1
# for i in range(len(a)):
#     ouput.append(a[i]+b[0])  # [ac]
#     ouput.append(a[i]+b[1])  # [ac]
# print(ouput)
# x = {'A': [2, 3, 6], 'B': [7, 10, 5]}  # {'A":[6,3,2],'B':[5,10,7]}
# val=list(x.values())
# key=list(x.keys())
# for i in range(len(val)):
#     temp=val[i]
#     val[i]=temp[::-1]
#     print(val)


#
# x = {'A': [2, 3, 6], 'B': [7, 10, 5]}
# # x={"a":[3,4,1],"b":[1,4,3]}#
# val=list(x.values())
# key=list(x.keys())
# for i in range(len(val)):
#     temp=val[i]
#     val[i]=temp[::-1]
#     print(val)


# out=dict(zip(key,val))
# print(out)
# for i,j in x.items():
#     temp=j
#     x[i]=temp[::-1]
# print(x)

# out={i:j[::-1] for i ,j in x.items()}
# print(out)

# for i in range(len(val)):
#     temp=val[i]  # ['a','b']


x = {'A': [2, 3, 6], 'B': [7, 10, 5]}
# x={"a":[3,4,1],"b":[1,4,3]}#
# val=list(x.values())
# key=list(x.keys())
# for i in range(len(val)):
#     temp=val[i]
#     val[i]=temp[::-1]
#     print(val)
#     out=dict(zip(key,val))
#     print(out)


#
#
# x={'A':[3,5,4],'B':[8,7,6]}
# for i,j in x.items():
#     temp=j
#     x[i]=temp[::-1]
#     print(x[i],end='')
# #


# lest=['anji','asha']
# lse=['java','python']
# z=zip(lest,lse)
# print(z)
# zip=dict(z)
# print(zip)

#
# li=['anji','a','b']
# lii=['10','20','30']
# z=zip(li,lii)
# print(z)
# z=dict(z)
# print(z)


# x={'1':['a','b'],'2':['c','d']}
# val=list(x.values())
# print(val)
# out=[]
# a=val[0]
# b=val[1]
#
# for i in range(len(a)):
#     out.append(a[i]+b[0])
#     out.append(a[i]+b[1])
# print(out)


# x = {'1': ['a', 'b'], '2': ['c', 'd']}  # ['ac','ad','bc','bd']
#
# val = list(x.values())
# print(val)
# ouput = []
# 0
# 1
# a = val[0]  # ['a','b']
# b = val[1]  # ['c', 'd']
# #  0     1
# for i in range(len(a)):
#     ouput.append(a[i] + b[0])  # [ac]
#     ouput.append(a[i] + b[1])  # [ac]
# print(ouput)

#
# let = ['abji', 'vijya',3]
# stu = {}
# stu = stu.fromkeys(let)
# print(stu)
# k=['a','bn']
# d={}
# f=d.fromkeys(k)
# print(f)


def mysum(a,b):
    x=a+b
    # print(x)
    return x
j=70
k=77
# out=mysum(j,k)
# out=mysum(5+5+5,3+4)
# print(out)