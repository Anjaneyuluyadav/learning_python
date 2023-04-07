# dictionary
# dic is a collection key and value pairs

# syntx
# x={'key1':val1,'key2':val2,'key3':val3}
#Properties
#duplicate keys are not allowed -> key is constant nd  values can be duplicated
# hetroginious keys and values are allowed
# we can fetch the values using keys (inserition order is not preserved)
# Dic is mutable  (we cn change the data)
# dic is dynmic -> u can give anything key and val
# indexing and slicing is not applicable


# #how to create dic
# x={}      # empty dic
# print(type(x))
# x=dict()     # this is recomanded
# print(type(x))
#
# a={}
# print(type(a))
# a={1:100,'A':200,10.5:'HELLO'}
# print(a)
#
#
# x={'A':100,'B':100,'A':30,'A':'python','B':"python"}
#
# # how to access dic values
# # we can get values using keys
# x={'A':100,'B':200,'C':'HELLO'}
# print(x['B'])
# print(x['C'])
# # #get
# print(x.get('C'))
# print(x.get('A'))
#
# print(x)
# print(x.values())
# print(x.keys())
# a=set()
# print(type(a))
# print(x['A'])
# print(x['B'])
#


#  # list
# a=[]
# print(type(a))
#
# a=list()
# print(type(a))# recommanded
# a=tuple()  #
# #
# # print(a)
# a.append(1)
# a.append(2)
# print(type(a))

# here A,B,C are keys nd 10,20,'python' is values
# /x=6
# print(x)
#
#
# x={'A':1,'B':2,'C':3}
# print(type(x))
# # Access the ele in dic
# # get
# z={100:"python",200:"JAVA",300:"C",100:"HI JAVA"}  # 100,200,300  keys
# # print(z[200])
# print(z[300])
# print(z.get(100))
# # print(z[300])
# print(z.get(300))


# a=[1,2,3]
# print(a[0])
# a=(1,2)
# print(a[0])
# a={1,3,4}
# a=list(a)
# print(a[0])


# z={100:"python",200:"JAVA",300:"C",100:"HI JAVA"}
# print(z.get(100))
# print(z.get(200))
# print(z.get(300))

# Create a dic using their names and marks input give from keyboard
# # dynamic
# student={} #dic()
# x=1
# while(x<=3):
#     name=input("Enter Student name :")  #
#     marks =int(input("enter marks :"))  #
#     student[name]=marks     #  way of create a dic
#     x=x+1
# print(student)

# x=[]
# for i in range(1,4):
#     y=input("ENTER VALUE :")
#     x.append(input("ENTER VAL"))
# print(x)



# del keyword
# del is useful for to delete the particuler key-val
# x={'A':100,'B':200,'C':300}
# x['D']=500
# #print(x)
# x['E']=1000
# print(x)
# del x['D']
# print(x)
# del x['A']
# print(x)

x={'A':[1,2,3,4],'B':(100,'python','ravi','narendra'),'C':[300,400]}
# print(x['A'])
# print(x['A'][2])
# print(x['B'][2])
# for key in x.keys():
#     print(x[key][0])
# print(x['A'][3]) # 4
# print(x['B'][1]) # python
# print(x.get('A')[2])
# print(x.get('B')[3])
# print(x.get('B'))
# print(x['A'])
# print(x.get('C'))
# print(x['C'])

# print(x.get('A'))
# print(x.get('B'))
# Dic  Functions
x={'A':[1,2,3,4],'B':(100,'python','ravi','narendra'),'C':300}

x={'A':[2,3],'B':(2,457),'C':['HI','HELLO']} #[2,3] ['HI','HELLO']
#pop  -> it removes the particuler key and val and returns the value of that particuer key
#print(x.pop('A'))
# x.pop('A')
# print(x)
# x.pop()
# print(x)
# z=x.pop('B')
# print(z)
# print(x)
# for key in x.keys():
#     print(x.get(key))


#print(x.popitem())
# x.popitem()
# print(x)
# popItem()  -> it wil the last key val pair in dic and return the last key ,val
# if dic is empty it will throw errorr
x={'A':[1,2,3,4],'B':(100,'python'),'C':300}
# print(x.pop('A'))
# x.pop('C')
# print(x)
# z=x.popitem()
# print(z)
# print(x)
# print(x.popitem()) # always remove the last key-value pair from dic
# print(x)

#x={'A':[1,2,3,4],'B':(100,'python'),'C':300}
# x.pop('C')
# print(x)
# x.popitem()
# # print(x)
# x={'A':[1,2,3,4],'B':(100,'python'),'C':300}
# x.clear() # x={}
# print(x)
x={'A':[1,2,3,4],'B':(100,'python'),'C':300}
#print(x.keys())
# y=list(x.keys())
# print(y)
# #print(x.values())
# a=list(x.values()) #[[1,2,3,4],(100,'python'),300]
# print(a)
# print(a[1][1])
#print(x.items())
# x={'A':100,'B':200,'C':300}
# z=list(x.items()) #[('A', [1, 2, 3, 4]),()]
# print(z)
# print(z[1][1][1])
x={'A':[1,2,3,4],'B':(100,'python'),'C':300} # update used for to update the value of perticuler keys and we can update new keys and values lso

# x.update({'A':1000,'B':2000})
# print(x)
# y={'A':100,'B':200,'D':300,'E':500}
# x.update(y)
# print(x)
# y.update(x)
# print(y)
# for i in range(len(z)):
#     print(z[i][0])

# x={'A':100,'B':200}
# x.clear()
# print(x)
#x={}
#
# x='Hel$%#lo$$55##'
# y=list(x)
# out=[]
# for i in range(len(y)):
#     if x[i].isalpha():
#         out.append(x[i])
#     elif  x[i].isnumeric():
#            if x[i] not in out:
#                out.append(x[i])
#     else:
#         if x[i] not in out:
#             out.append(x[i])
#
# print(out)

# clear
# it removes the all elements in dic
#x.clear()   # x={}
# x={}
# print(x)
# keys() -> it returns the all the keys in dic
# z=list(x.keys())
# print(z)
# print(z[0])
# vaues()  -> it returns the all the values from dic
# z=list(x.values())
# print(z)
# print(z[1][1])

# items() -> it wil return the list of tuples representing key and val pairs

# z=list(x.items())
# print(z)
# print(z[0][0])
# print(z[1][1][1])

# ass1

#x=[('A', [1, 2, 3, 4]), ('B', (100, 'python')), ('C', 300)]   # output ['A','B','C']
#
# x={'A':1,'B':2}
# print(id(x.pop('A')))

# copy  -> copy the ele from one dic to another dic
x={'A':[1,2,3,4],'B':(100,'python'),'C':300}
# x.update({'A':1000})
# print(x)
# y=x
# print(y)
# y=x.copy()
# print(y)
# update -> we can update the particuler value and we can upate one dic to another dic

# y={'C':2000,'D':'JAVA'}
# x.update(y)
# print(x)
#
# y.update(x)
# print(y)
# setdefault   -> setdefault(key,Val)   # val is value
# if key is already available then this function returns the value of that perticuler key
# if key not exits it wil append the key to the dic
# x={'A':[1,2,3,4],'B':(100,'python'),'C':300}
# print(x.setdefault('D',200))
# print(x.setdefault("E"))
# print(x)
# x.setdefault('D',3000)
# print(x)
# print(x.setdefault('E',200000))
# print(x.setdefault('F',1000000000))
# print(x)



# x.setdefault('E',1000)
#print(x.setdefault('B'))
# print(x)

# Fromkeys -> it wil two args # syntax : x.fromkeys(key,val)  val is optional
# we can updte common val for the all the keys of existing dic
# using fromkeys we can able to create new dic passing set of keys and val
#
# x={'A': [1, 2, 3, 4], 'B': (100, 'python'), 'C': 300, 'D': 200}
# x=x.fromkeys(x.keys(),100)
# print(x)
# a=10
# print(a)
# del a
# a=200
# print(a)



#
# print(x.fromkeys(x.keys(),1000))
#
# z=x.fromkeys(x.keys(),2000)
# print(z)
# #
keys=['a','b','c','d','e']
val=100 #list,set,tuple,str
z=dict.fromkeys(keys,val)
print(z)

#
# a={}
# x=['A','B','C']
# y=[100,200,300]
# out={'A':100,'B':200,'C':300}  # {100:'A',200:'B',300:'C'}
# x=list(out.keys())
# y=list(out.values())
# z=list(zip(y,x)) #[(100,'A'),(200,'B')]
# z=dict(z)
# print(z)
# x=[('A',200)]
# y=dict(x)
# print(y)
# list1=['A','B','C']  # list2 =[100,200,300]  -> x={'A':100,'B':200,'C':300}

# x=[1,2,3]
# y=['A','B','C']
# z={}
# for i in range(len(x)):
#     z[y[i]]=x[i]
# print(z)

# z=list(zip(y,x))
# print(z)
# z=dict(zip(y,x))
# print(z)


#
# keys={'a','b','c','d','e'}
# val=100
# z=dict.fromkeys(keys,val)
# print(z)


#x=[1,2,3,4,5]   #[1,2,5,4,3]




# Dictionaries:
# 𝙰𝚜𝚜𝚒𝚐𝚗𝚖𝚎𝚗𝚝 𝚘𝚗 Dictionaries
# Input: x ={“A”:100, “B”:200, “C”:300, “D”:200}
#        Output: x= {“A”:110, “B”:210, “C”:310, “D”:210}  # add 10 to the values of dictionary
# Input: x ={“A”:1, “B”:2, “C”:3, “D”:4}
# Output: [(1,”A”), (2,”B”), (3,”C”), (4,”D”)]
# Input: x = “ABCDABCABE”
# # Output: {“A”:3, ”B”:3, ”C”:2,”D”:1,”E”:1}
#
# x={'A':100}
# y={'B':200}
# x.update(y)
# print(z)

# out={A:100,'B':200}


# nested dic : dic inside the dic is called nested dic

# x={'A':{'x':100,'y':200},'B':[1,2,3],'C':{'i':'python','j':'java'}}
#
# print(x['B'])
#
# print(x['A']['y'])
# print(x['B'][-1])
# print(x['B'][2])
# print(x.get('C')['i'])
# x ={'A':100, 'B':200, 'C':300,'D':200}      # {100:'A',200:'B',300:'C'}
# keys=list(x.keys())
# print(keys)
# values=list(x.values())
# print(values)
# z=dict(zip(values,keys))
# print(z)
# x={i:i*i for i in range(1,6)}
# print(x)
# x={'A':1,'B':2}
# squares={i:x[i]*10 for i in x.keys()}
# print(squares)

# # a={}
# for i in range(len(values)):
#     a[i]=keys[i]



# values=[i+10 for i in values]   #list comprehension
# print(values)
# # method -2
# for i in range(len(values)):
#     values[i]=values[i]+10
# print(values)

# z=dict(zip(keys,values))   # ()
# print(z)
# method -2
# for key,val in x.items():
#     print(key,val)
#     x[key]=val+10
# print(x)

#
# x={1,2,3}
#
# for i,j in enumerate(x):
#     print({i,j})
#
#
# x={'A':10,'B':20}     #    x={'A':110,'B':220}
# for i,j in x.items():
#     x[i]=j*j
# print(x)
#
