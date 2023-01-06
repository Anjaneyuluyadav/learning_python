# List : its a collection of hhetroginious elements
#duplicates r allowed
# insertion order is preserved
# it is mutable (we can chnage the data)
# the forward dir inde starts from zero backword dir starts from -1
# its growable nature (we can add n num of ele)
# the list is enclosed with []

# syntax : varname =[]

# x=[] # -> its called empty list
# print(type(x))
# x=list()  # recommanded to use
# print(type(x))
# how to revrerse the list
x=[10,3,6] # [6, 3, 10]
# print(x[::-1])
# temp=list(reversed(x))
# print(temp)
# for i in x:
#     print(i,end=' ')
# var=sorted(x)     # it will sort te elements in assedin order
# print(var)
#
# var=sorted(x,reverse=True)     # it will sort te elements in assedin order
# print(var)

# x.reverse()
# print(x)



x=[30,2,5,8]
# x.sort()
# print(x)
# var=list(sorted(x))
# print(var)
# var=list(sorted(x,reverse=True))
# print(var)

# max :
# print(max(x))
# x.sort()
# print(x[len(x)-1])
# print(x[-1])

x=[60,2,400,5,70,8]
# y=list(sorted(x))
# print(y)
# print("max",y[-1])
# print("mkin",y[0])
# print("min",min(x))
# print("max",max(x))
x=[60,2,400,5,70,8]
# max=x[0]   # max =60  # max =70
#
# for i in range(len(x)):
#     if x[i]>max:
#         max=x[i]
# print("max ele in list is :",max)


# max    i    x[i]    x[i]>max
# 60     0    60       false
# 60     1   2        false
# 60     2    400     true
# 400   3    5        false
# 400   4    70       false
# 400   5    8       false





# x=[60,2,400,5,70,8] # [400,5,70]
# # syntax : [stindx:endix:seppingg]
# #print(x[2:5])
# print(x[::2])
#print(x[-1])
# print(x[len(x)-1])

# nested list : list inside te list called nested list#
#      0 1  2    0   1  2    0 1   2
#x=[[10,20,30],[40,50,60],[70,90,100]]
#      0          1          2

x=[[10,20,30],[40,50,60],[70,90,100]]   #[20,50,90]
# print(x[-1])
# print(x[len(x)-1])
# print(x[1])
# print(x[1][1])
# print(x[2][1])

# print(x[0][-1])
# print(x[1][-1])
# print(x[2][-1])
# for i in range(len(x)):
#     print(x[i][-1])
# print(x[1][1:])
# print(x[0][1:])
# print(x[2][:2])
# print(x[2][:len(x[2])-1])

# x=[[10,20,30],[40,50,60],[70,90,100]]
# # for i in range(len(x)):
# #     print(x[i][::-1])
# for i in range(len(x)):
#     temp=x[i]             #[10,20,30]
#     for j in range(0,len(temp)):
#         print(pow(temp[j],2),end=' ')
#     print()

# append -> usedd for yto add te element into te list
# append add te elements at last
# x=[1,2]
# x.append(3)  # 2
# x.append(10) # 3
# print(x)
# x.append([40,50,60]) #4
# print(x)
# x.append({"j",'k'})
# print(x)
# x.append(("j",'k'))
# x.append({'A':200,'B':400})
# print(x)
# print(x[-1])
# print(x[4])
# print(x[-4])
# insert ->  ibsertt useful for to insert the element at perticuler index
# x=[1,3,5,7]
# x.insert(2,'HI')
# print(x)    # len(5)

# x.insert(len(x),"HELLO")
# print(x)
#
# x=[[1,2,3],[4,5,6]]
# temp=x[1]
#
# temp.insert(1,'HI')
# print(temp)
# x[1]=temp
# print(x)

# append -> add the ele at last   # insert -> insert the ele at desired position
# remove -> removes thhe element from the list if ele is present if it not present it wil ggive thhe error
# suppose ele is exits mor than one time it will remove the frst occurence of the element
x=[1,2,3,4,3]
# print("len :",len(x))
# x.remove(3)
# print(x)
# print("len :",len(x))
# x=[1,2,3,4]
# if 2 in x:
#     x.remove(2)
#     print(x)
# else:
#     print("ele is nt exits")
# index => used to et index of te element if it is presnt ,if ele is not presrtn it will ggive error\
# suppose ele exuts mor than one time it will give index of frst occuerance of te elemerny
# x=[1,4,[2,5,7],5,6,4]
# print(x.index(4))
# print(x.index(5))
# print(x.index(x[-1]))
#print(x.index(10))
#print(x.index([2,5,7]))




# out=list()
# for i in range(len(x)):
#     out.append(x[i][1])
# print(out)

# x=[[10,300,22],[4000,50,600],[70,900,10000]]   #[300,4000,10000]
#
# out=list()
# for i in range(len(x)):
#     out.append(max(x[i]))
# print(out)

# 1-100 []
# x=list(range(1,10))
# print(x)
#
# # synatax : range(stinx,endindx,stepping)
# x=list(range(0,11,2))
# print(x)

# x=[0,1,1,0]  #  0110=6
# count=1
# s=0
# for i in range(len(x)):
#     if x[i]==1:
#         z=pow(2,count)
#         s=s+z
#     count=count+1
# print("integer of bin list",s)


# x="1010"
# print(int(x))
# x=10
# print(bin(x))

x=[1,0,1,0,1,0]  # [111000]
# #print(sorted(x,reverse=True))
# print(list(reversed(x))) # [::-1]
# a=list()
# b=list()
# out=list()
# for i in range(len(x)):
#     if x[i]==1:
#         a.append(x[i])
#     else:
#         b.append(x[i])
# out=a+b
# print(out)

# x=["Hi","Hello","java"]  #"hI hELLO JAVA"
#
# y=" ".join(x)
# print(y)
# y=y.swapcase()
# print(y)

# x=list(range(1,11)) #get all even num using list comphresnsion
# # synatax :[var for in iterobj if con]
# z=[i for i in x if i%2==0]
# print(z)

# x=[3,4,2] # [27,64,4]
# out=[]
# for i in range(len(x)):
#     out.append(pow(x[i],x[i]))
# print(out)

x=[1,4,6,7,4,7]
#countt -> used to count te ele how many times it is exits
# if ele is not exits it will rturn 0
# print(x.count(4))
# print(x.count(7))
# print(x.count(1))
# print(x.count(0))
# sort -> used to sort the list
# by default it will sort thr list elements uin assedninf order
# x.sort()
# print(x)
# x.sort(reverse=True)
# print(x)
x=[1,4,6,7,4,7]

# print(list(sorted(x)))
# print(list(sorted(x,reverse=True)))

# Reverse -> used for to revrse the list
#print(x[::-1])
#print(list(reversed(x)))
# x.reverse()
# print(x)
# clear _-> used to clear the list remove all the elements from the list
# x=10
# print(x)
# x=0
# print(x)
x=[1,4,6,7,4,7]
#x.clear()  # x=[]
#x=[]
#print(x)
#copy -> copy the list from one variable to anoter variable
#y=x
# y=x.copy() #y=x
# print(y)
# print(type(y)
# pop -> pop is useful to remove the last element and it will return the element
# if we provide the index it will remove the perticuler index value
# print(x.pop())
# print(x)
# print(x.pop())
# print(x)
# print(x.pop(10))
# print(x)

# remove                                          pop
# remove will te frst occurence of             # pop will remove the last ele by default
#the perticuler ele
# suppose ele is not exits iy will give error  # if index is not exits it will throw the error
# it deals with element                        # it deals with index
# it cant return any val                       # it will return the removed ele

#extend -> extend udsed for for extends the list (it wil increase the index order)
# x=[1,2,3,4]
# y=[5,6,7,8,10]
# y=(3,5)
# y={7,8}
# y={'A':10,'B':40}
# x.extend(y)  # [1,2,3,4,5,6,7,8,10]
# print(x)
# print(x.index(7))
# how to concatinate two list
# usingg + ope we can
# x=[1,3]
# y=[2,4]
# print(x+y)
# '*' is repitative ope we can print the list num of times
# x=[1,2]
# print(x*3)
# x=[1,2]
# y=[1,3]
# print(x==y)
# x=[1,2]
# y=[1,2]
# print(x==y)
# x=[1,2]
# y=[1,2,3]
# print(x==y)

# x=[[1,2,3],[4,5,6],[7,8,9]]
#
# print(x[2][1])
# print(x[1][2])
# print(x[0][1])
#List comphrehension : it is very easy and compact way to create the list objects from any iterable objects like(list,tuple,dict,range) based on some cond
#syntx :[Expression for ele in iterableobj if condition]
x=[1,2,4]
# y=[ele for ele in x]
# print(y)
# y=[ele*ele for ele in x]  # [1,4,16]
# print(y)
# y=[]
# for ele in x:
#     y.append(ele*ele)
# print()
# y=[i for i in range(1,11) if i%2==0]
# print(y)
# y=[]
# for i in range(1,11):
#     if i%2==0:
#         y.append(i)
# print(y)

# x=['Ab','Cd','Ef'] # [ab,cd,ef]
# y=[i.lower() for i in x]
# print(y)
x=[1,2,3,1,3,5] # rmemove the duplicates from the list [1,2,3,5]
out=[]                  # [1,2,3]
y=[out.append(i) for i in x if i not in out]
print(out)
