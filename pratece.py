# class test:
#     pass
# # calling
# t=test()
# print(t)
#
# # insercting
# t.x=12
# print(t.x)
# test.y=20
# print('x val is:',t.x)
# print('y val is:',t.y)
# print('x val is:',test.y)
#
# # updating
# # t.x=77
# # t.y=88
# # print('x val is:',t.x)
# # print('x val is:',t.y)
# # print('x val is:',test.y)
# #
# # # deleting
# # del t.x
# # print('x val is:',t.y)
#
# h=5
# class A:
#     x=20
#     def sa(self):
#         x=10
#         self.x=12
#         print("instance:",self.x)
#         print("local:is",x)
#         print("static value:",t.x)
#         print("static value:", A.x)
#
#     def sa1(self):
#         print("sta",A.x)
#         print("static value:", t.x)
#         print("local value:",self. x)
#
# t=A()
# t.sa1()
# t.sa()
# print(t.x)
# print("static value:", h)

class test:
    course='python'
    def fun(self):
        self.a=int(input("entry any"))
        self.b=input("eny")

    def getval(self):
        print("instance val:",self.a)
        print("instance val:", self.b)
        print("static val:", t.course)

# t=test()
# t.fun()
# t.getval()
#
# t2=test()
# t2.fun()
# t2.getval()
#
# t3=test()
# t3.fun()
# t3.getval()
class test:
    def m1(self,x,y):
        self.a=x
        self.b=y
        print("instance val is",self.a)
        print("instance val is", self.b)
        print("instance val is", self)

    @classmethod
    def getvalue(cls,x,y):
        print("class mm",cls)
        print("instance val is",cls.x)
        print("instance val is", cls.y)
        # print("instance val is", test.x)
        # print("instance val is", cls.y)

    @staticmethod
    def m2():
        pass

# t=test()
# t.m1(2,3)
# print(type(t))
# t.getvalue(3,5)


# inheritence:class

class superA:
    def method1(self,x,y):
        print("instance md1")


        self.x=x
        self.y=y
        print(self.x)
        print(self.y)
class subB:
    def method2(self):
        su=superA()
        su.method1(34,65)

        print("instance md 2")
# t1=subB()
# t1.method2()




# @classmethod inheritence

class superA:
    @classmethod
    def method1(cls,x,y):
        print("this is cla md")
        print("this is cla md SA",cls)
        print("cls md of sa val :",x)
        print("cls md of sa val :", y)

class subB:
    def method2(self):
        superA.method1(10,30)
        print("instance val md2 SB")
# sb=subB()
# sb.method2()


# single inheritences
class father:
    def house(self):
        print("this is a father's house")
class son(father):
    def car(self):
        print(" two val or propertives")
        print("this my car son ")

# sn=son()
# sn.car()
# sn.car()
# sn.house()


# multilevel inheritences
class godfather:
    def some_propertives(self):
        self.x=10
        self.y=20
        print(self.x)
        print(self.y)
class father(godfather):
    def house(self):
        print("this is a father's house")
class son(father):
    def car(self):
        print(" two val or propertives")
        print("this my car son ")

# sn=son()
# sn.car()
# sn.house()
# sn.some_propertives()




class stu:
    def setstu(self):
        self.d=stu.dom()
        self.g = stu.marks()
        self.f=stu.marks
        self.name=input("entre name:")
        self.no = input("entre no1:")


    def getstu(self):

        print("name is a:",self.name)
        print("entre no is a:",self.no)
        print("marks val is :",self.marks)
        print("marks val is :", self.g())
    class dom:
        def setdom(self):
            self.dd = input("entre name:")
            self.mm = input("entre name:")
            self.yy = input("entre name:")
        def getdom(self):
            print("print the dom values")
            print("dd/mm/yy/{}/{}/{}".format(self.dd,self.mm,self.yy))

    class marks:

        def setdom(self):
           self.m1=input("mathes:")
           self.m2=input("english:")
           self.m3=input("secince:")



        def getdom(self):
           print("marks",self.m1)
           print("marks", self.m2)
           print("marks", self.m3)

# su=stu()
#
# su.setstu()
# su.getstu()
# su.dom()
# su.marks()



import sys
x=int(sys.argv[1])
y=int(sys.argv[2])
s=x+y
print("type of :",s)






