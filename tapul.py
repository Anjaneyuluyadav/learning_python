# x=10,2,22,34,5,10,1,2,2
# sno=2
# li=len(x)
# i=0
# while i<li:
#     if i==sno:
#         i=i+1
# #     print()
# n=4
# i=1
# for o in range(1,n+1):
#     for i in range(1,n+1):
#         i=i+1
#         print(i ,end="")
#     print("")

    # tuple
    # tuple is same like a list but we can't chnage the values in tuple  [read only]

    # where to use  -> if u want to make your data is constant then we can go with tuple
    # tuple dupicates are allowed
    # hetrogenious(different type) elemnts and duplicate are allowed
    # +Ve and -ve index

    # +ve index satarts from 0 and -Ve index starts from -1(backword direction)

    # parut recommanded to useanthis are optional b

    # tuple index also start from zero

    # syntax :
    # tuple_name=1,2,4
    # print(type(tuple_name))
    # tuple_name=tuple()    #
    # print(type(tuple_name))
    # x=()
    # print(type(x))
    # x=1,
    # print(type(x))
    # x=(1,)
    # print(type(x))

    # x=10,20,30
    # print(x)

    # x=10
    # print(type(x))
    # x=10, #()
    # print(x)
    # print(type(x))
    # x=(10,)
    # print(type(x))

    # Syntax
    # variabe =1,
    # print(type(variabe))
    #
    # x=(1,)
    # print(type(x))

    # x=1,2,3
    # print(x)
    # print(type(x))
    #
    # x=(1,2,3)  # recommnded to use
    # print(x)
    # print(type(x))
    # create a tuple
    # a=[]
    # print(type(a))
    # a=list()
    # print(type(a))
    # a=()
    # print(type(a))
    # a=tuple()
    # print(type(a))
    # a=(3,5)
    # a=("python",)
    # print(type(a))
    #
    # a="python",

    # how to access ele from tuple
    #
    # x=(1,2,3,4,55) #  x=(1,2)
    # print(x[-1])
    # print(x[len(x)-1])
    # print(x[4])

    # a=(1,2,3,4,2,3,10,200,300,2,4,5,2) # index ,count
    #
    # print(a[4])
    # print(a[7])

    # print(a.index(5))
    # print(a.index(2))
    #
    # print(a.count(1))
    # print(a.count(4))
    # # print(a.index(300)) # 1
    # print(a.index(300)) # 2
    # a=(1,2,3,4,5,2,2,3,4) # index ,count
    # print(a)
    # print(a[0])
    # print(a[1])
    # print(a[-1])
    # print(a[-2])
    # print(a[1:4])

    # give input from keyboard
    # y=list()
    # for i in range(5):
    #     y.append(int(input("Enter  val :")))
    # #
    # print(y,type(y))
    #
    # x=tuple(y)
    # print(x,type(x))
    # how to create a tuple
    #
    # y=list(range(1,11))  # mutable
    # print(y)
    # #
    # print(y[0])
    #
    # y[0]=1000
    # print(y)
    #
    # x = (1, 10, 20, 30, 20)  # [10,100,200]
    # y=list(x)
    # y=[i*10 for i in y ]
    # print(y)
    # print(x.index(20))
    # print(x.count(20))

    # accessing ele from tuple
    # x=tuple(range(1,11)) # immutable (1,2,3,4,5,6)   9,10
    # print(x)
    # print(type(x))

    # print(x[4])
    # print(x[6])
    # print(x[-2])
    # print(x[-4])
    #
    # print(x[2:5])
    # print(x[8:])
    # print(x[8:11])
    # print(x[1::2])

    # tuple functions
    #
    # x = (1, 2, 3, 4)
    # y = (4, 5, 4, 5)

    # z=(5,7,7,9)
    # print(x+y) #(1,2,4,5)
    # print(x*2)
    # z=[]
    # x=list(x)
    # y=list(y)
    # for i in range(len(x)):
    #     z.append(x[i]+y[i])
    # z=tuple(z)
    # print(z)

    # for i in x:
    #     print(i,end=" ")
    # print(x[0])
    # x[0]=10000
    # print(x)

    # x=[1,4,5,6,8]
    # y=tuple(x)
    # print(y)
    # + concantation

    # x=[1,4,10,2,5]
    # y=sorted(x)  #[1,2,4,5,10]
    # print(type(y))
    # print(min(x))
    # print(max(x))
    # #
    # x=(1,2,3,4,54,4,5,3)
    # y=tuple(sorted(x))
    # print(y)
    # #
    # z=tuple(sorted(y,reverse=True))
    # print(z)

    # y=(4,5,6)
    # z=x+y
    #
    # a=list(x)
    # print(a)
    # a[0]=1000
    #
    # x=tuple(a)
    # print(x)
    # multiplication
    # print(x*5)

    # count
    # x=(1,2,3,4,54,4,5,3)
    # print(x.count(4))
    #
    # # index
    # print(x[-4])
    #
    #
    # len
    # print(len(x))
    #
    # x=(20,2,10)
    # # sorted
    # print(sorted(x))
    # print(min(x))
    # print(max(x))
    #
    # c=[]
    # c.extend((10,20,30))
    # print(c[0])

    # cmp  ==
    # x=(1,2,3,10)
    # y=(1,2,3,11)
    # z=[]
    # for i in x:
    #     if i in y:
    #         z.append(i)
    # print(z)

    # x=[1,3,5,2]
    # y=[1,2,3,5]   # con1 len need to check

    #
    # x="aAB" #65+66 =131
    # y='BAa' #66+65 =131

    # Asss1
    # Wap a progrm to change the tuple values

    # x=(10,2,3,5)-> each ele multifly by 10   (100,20,30,50)

    # ass2 :
    # x=[1,2,3,4] -> [3,5,7]

    # x = 'JAVA'
    # x=list(x)
    # j 1
    # A 2
    # V 1

    # for i in set(x):
    #     if i in x:
#     #         print(i,x.count(i))
# tu=10,20,30,40,50
# print(type(tu))
# li=len(tu)
# pos=2
# new=[int(input("eny"))]
# if pos>=0 and pos<=li:
#     if pos<li:
#        print("valied")
#        f=tu[0:pos:1]
#        s=tu[pos:1:]
#        t=f+tuple(new)+s
#        print(t)
#     else:
#         print("invallied")
#

def tips_transpose(lst):
  return list(zip(*lst))

print(tips_transpose([[2, 5, 6], [1, 3, 5], [8, 10, 12], [7, 9, 11]]))
