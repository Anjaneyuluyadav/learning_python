# class :class is a collection of methods,objets,variables
# synatax : class "classname" :  Ex :# class A :
#object : object is a blue print of class
# syntax : obj=classname()  # out =A()
# __init__() : __init__() is default method in the class
#__init__()  is a constuctor
# when ever we create the obj init method wil call by defult
# init method useful for to initise the values
#__init__() wil execute only once per the object
# __init__() will take atleast onw argument that is self
# the __init__() useful for to intilise the variables
# self : self a default parameter to the method, it is always pointing to the current obj address , we can initiise the varible using self
# every method in class is starts with keyword called def
# class A:
#     def __init__(self,a,b):
#         self.x=a
#         self.y=b
#         print("caling init method")
#         print(self.x)
#         print(self.y)
#     def hello(self):
#         print("HI hello")
#         print(self.x)
#         print(self.y)
#     def java(self):
#         print(self.x)
#         print(self.y)

# out=A(10,20)
# out.hello()
# out.java()
# obj1=A()
# obj2=A()

# class B:
#     def __init__(self,a,b):
#         self.x=a
#         self.y=b
#     def sum(self):
#         return self.x+self.y
# out=B(20,30)

# print(out.sum())
#types of variables
# instance variables :
# the vribale which is vrified object to object such type of variabes clled instance var
# for every object saparate copy of instance variable will be created
# where we can access instance variables:
#1) inside the constructor(__init__ method)
# inside the instance methiod
#outside of the clss using object refernce

# class B:
#     def __init__(self,a,b):
#         self.x=a
#         self.y=b
#     def sum(self):
#         return self.x+self.y
# out=B(20,30)
# obj=B(50,60)
# print("the values of out",out.x,out.y)
# print("the values of out",obj.x,obj.y)

#static variables or classvar : The varible is not varified obj to obj
# we can delcare these varibles inside class but outside of the methods such type of variables clled static var
# we have to delcare this variabls using class name
# where we cn access
# inside the constryctor using classname
#inside the instance method using classname
#inside the class method using classname or cls
# inside the static method using class name
# outside class using class name

# class B:
#      z=100
#      def __init__(self):
#          print("inside the construutor :",B.z)
#      def hi(self):
#          print("inside the instance :",B.z)
#      @classmethod
#      def cls_method(cls):
#          print("inside the class method :", B.z)
#          print("inside the class method :", cls.z)
#      @staticmethod
#      def static_method():
#          print("inside the sttic method :", B.z)
# out=B()
# out.hi()
# out.cls_method()
# out.static_method()
# print("outside the class :",B.z)
# local variable : the variable which is declared inside the method is clled local variable
# the scope of the loacal varible is inside the method only
# it cant be acess utside of the method

# class A:
#     def Hi(self):
#         a=100
#         print("Hi method data ",a)
#     @staticmethod
#     def Hello():
#         a=10
#         print("Hi method data ",a)
#     @classmethod
#     def Hello(cls):
#         a=200
#         print("Hi method data ", a)
#
# obj=A()
# obj.Hi()
#print(out.a)

# three types of methods are there
# instance method
# class method
# static method
# instance method
# the method which contains self as a default parameter is clled instance method
# we ccn acess all instance variabls inside the instane method
# we have to cll instance method using object refernce
# static/clss var can be access inside the instance method using class refernce
class C:
    x=200
    def __init__(self):
        self.y=100
    def python(self):
        self.a=300
        print("Cls var :", C.x)
        print("Instance method var :",self.y)
    def java(self):
        print("python method var",self.a)
        print("Cls var :",C.x)
        print("Instance method var :", self.y)
    def CPP(self):
        print("python method var", self.a)
        print("Instance method var :", self.y)

# obj=C()
# obj.python()
# obj.java()
# obj.CPP()

# class method
# inside the method iplementation if we r using only classvar(static var) then such type of methods caled cls method
#we can declare class method usng @classmethod decorator
# for class method we have to provide cls as a parameter (when we create automatically it will come)
# we can class method using classname or object refernc
# class C:
#     x=200
#     @classmethod
#     def CPP(cls):
#         print("python method var", cls.x)
#         print("Instance method var :", C.x)
# out=C()
# out.CPP()
# C.CPP()
# print("clss var :",C.x)
# static method :
# in general these methods are utility methods
# inside the static method we wont use any cls var or instance var
# we have declare static method using @static method decorator
# we can call static method using classname or object refernc
# static method useful for to access static variables
# for class method and static method obj is not required
# class C:
#     x=200
#     @staticmethod
#     def CPP():
#         print("Instance method var :", C.x)
# out=C()
# out.CPP()
# C.CPP()
#passing one class members to another classs
# class student:
#     def __init__(self,x,y):
#         self.name=x
#         self.Rno=y
#     def Print_student_data(self):
#         print("Student name :",self.name)
#         print("Student Rno :", self.Rno)
# obj=student("ANJI",1)
# obj.Print_student_data()
# class Teacher:
#     def __init__(self):
#         self.school_name="NARAYANA"
#     def Access_Student_Data(self,obj1):
#         print("Student name :", obj1.name)
#         print("Student Rno :", obj1.Rno)
#         #studentobj.Print_student_data()
#         print("Schoolname :",self.school_name)
# out=Teacher()
# out.Access_Student_Data(obj)

