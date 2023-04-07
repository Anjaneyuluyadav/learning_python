# set :
# set is a collection of etronious elements
# duplicates r not allowed
# insertion order is not preserved
#set ele we ave to represents in curly braces
# indexin and slicin is not allowd
# we can apply mathamatical operations on set

# hoe to define the set

# x=[] # x=list()
#x=() # x=tuple()
# x=set()
# print(type(x))
# how to access the ele
# we cant fetch the perticuler ele from th set becuse set does nit have indexingggg
# x={1,2,4}
#
# for i in x:
#     print(i,end=' ')

s1={1,6,6,2,2,5,78,3}
s2={2,6,3,3,5,7,0,94}
s3=s1.symmetric_difference(s2)
print(s3)



# x=set(range(1,5))
# for i in x:
#     print(i,end=' ')

# set functions
# x={1,2,6,7}
# # add -> add used for to add the ele into the set
#
# x.add(100)
# print(x)
# update -> usinggg update we can add multiple ele at atime
# x={1,2,6,7}
# x.update({10,20,30},{40,70})
# x.update(range(1,6),range(7,9))
# print(x)
# copy -> used for to copy the elements from one variable to another

# y=x.copy() #y=x
# print(type(y))
# print(y)
# pop- -> removes the random ele fron the set and retuen the ele which its ggoing to remove

x={1,4,5,2,3,7,4}
# x.pop()
# x.pop()
# print(x.pop())
# print(x)
# x.pop(5)
# print(x)

# x=[3,4,56,7]
# x.pop(2)  -> provide index for which ele u want to remove
# print(x)
# remove ->  remove used for to remove the specific ele if ele is present , if it is not present it wil trow the error
x={1,4,5,2,3,7,4}
# x.remove(4)
# print(x)
#x.remove(10)
# # discard -> remove used for to remove the specific ele if ele is present , if it is not present it will not trow the error
# x={1,4,5,2,3,7,4}
# x.discard(44)
# print(x)
# clear -< it remove the all the ele
# x=[1,3,4]
# x=[]
x={1,4,5,2,3,7,4}
# x.clear()
# print(x)
# print(len(x))
# mathamaticl operations

# union ->  we can use this functionm to return all thhe ele from both sets
# x={1,2,1}
# print(len(x))
# y={3,4,3}
# print(y)
# print(x.union(y))
# intersection : retuens the commonm ele in both sets

# x={1,2,1,3,4}
#
# y={3,4,3}
# print(x.intersection(y))

# difference _-> retuns the  elemensts in one pertixuler ser

# x={1,2,1,3,4}
#
# y={3,4,3,10,11}
# print(x.difference(y)) # print(x-y)
# print(y.difference(x)) #print(y-x)
# print(x-y)
# print(y-x)

# symmetric diff -> retuens the diffeeent ele from both sets


# x={1,2,1,3,4}
#
# y={3,4,3,10,11}
# print(x.symmetric_difference(y))


# set comphreension

# syntx :" {expression for loop in (iterableobj) if con}

# x={1,3,5,6}
#
# out={pow(i,2) for i in x}
# print(out)


#  evn num from set
# out={i for i in range(1,11) if i%2==0}
# print(out)

#
# x={1,2,3,4}
# y={5,6,7,8}    # {1,4,3,16,5,36,7,64}
# x=x.union(y)
# print(x)
# out={pow(i,2) for i in range(1,6) if i%2==0}   # [
# print(out)

#
out=set()
for i in range(1,6):
    if i%2==0:
        out.add(pow(i,2))
print(out)


