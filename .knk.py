# HAS -A Relationship
# we can able to acess one class data into another class
# by creating one class object inside the another class
#
# class A:
#     def __init__(self,student_name,Rno):
#        self.name=student_name
#        self.Rno=Rno
#     def A_print_info(self):
#         print('STUDent name :',self.name)
#         print("Rno :",self.Rno)
# #obj=A("NAAGG",123)
# #obj.print_info()
#
# class B:
#     def __init__(self,student_name,Rno):
#        self.name=student_name
#        self.Roleno=Rno
#        self.A_obj=A("NAA",7777)
#     def print_info(self):
#         print('STUDent name :',self.name)
#         print("Rno :",self.Roleno)
#         self.A_obj.A_print_info()
# obj1=B("PYTHON",123)
# obj1.print_info()

# ineritance :getting the properties of super class from sub class
# the main advantage of inheritaance is we  no need to rewrite the code.
# syntax :

# class A:
#     def fun1(self):
#         # st1
#        # st2
# class B(A):
#     def fun2(self):
#         #st3
#        #st4

# obj=B()
# obj.fun1()
# obj.fun2()

#is-A Relationsjip :wat ever data which is present in parent class by default avialable to the child class
# we no need to rewrite the code
# the main advantage is code reusablility>

# class A:
#     x=100
#     def hi(self):
#         print("HI to class A")
# class B(A):
#     pass
#
# obj=B()
# obj.hi()
# print(obj.x)

# single_inheritance : the conceprt of inherting properties from one parent class to one child class is called sigle inheritance

# class A :     # parent class
#     def hi(self):
#         print("Hi to class A")
#     def hello(self):
#         print("Hello to class A")
# class B(A):   # child class
#     def student(self):
#         print("my students r good")
# obj=B()
# obj.hi()
# obj.hello()
# obj.student()

# multilevel inhritance : the concept of inherting peroperties from mutiple classes to single class one after another is called multilevel inheritance
#syntax :
# class A:
#     data
# class B(A)
#     data
# class C(B)
#     data
# class D(C)
#     data


# class A:
#     def hi(self):
#         print("hi belongs to class A")
# class B(A):
#     def hello(self):
#         print("hello belongs to class B")
# class C(B):
#     def hello_hi(self):
#         print("hello_hi belongs to class C")
# obj=C()
# obj.hi()  # A class data
# obj.hello()
# obj.hello_hi()

# hierarchical inheritance : the concept of inherting peroperties from one class to mutiple class which are present at same level called hierarchical inheritance

#syntax :
# class A:
#     data
# class B(A)
#     data
# class C(A)
#     data
# class D(A)
#     data

class A:
    def hi(self):
        print("hi belongs to class A")
class B(A):
    def hello(self):
        print("hello belongs to class B")
class C(A):
    def hello_hi(self):
        print("hello_hi belongs to class C")
# obj=A()
# obj.hi()
# obj_B=B()
# obj_B.hi()
# obj_B.hello()
# obj_C=C()
# obj_C.hello_hi()
# obj_C.hi()

# mutiple inheritance : the concept of inhrriting properties fromm mutiple classes to  into single class   that is called mutiple inheritance

# syntax :
# class A:
#     data
# class B:
#     data
# class C:
#     data
# class D(A,B,C)
#     data

class A:
    def A_hi(self):
        print("class A hi")
class B:
    def B_hello(self):
        print("class B hello")

class C:
        def C_frnds(self):
            print("class C hi_Frnds")

class D(A,B,C):
    def D_data(self):
        print("class D data")

# obj=D()
# obj.A_hi()
# obj.B_hello()
# obj.C_frnds()
# obj.D_data()

#hybrid_inhrritance :  the conmbination of single,multiple,hierarhical  inhritance is called hybrid inhheritance

#sntax :
# class A:
#     data
# class B:
#     data
# class C(A,B):
#     data
# class D(C)
#   data


class A:
    def A_hi(self):
        print("class A hi")
class B:
    def B_hello(self):
        print("class B hello")

class C(A,B):
        def C_frnds(self):
            print("class C hi_Frnds")

class D(C):
    def D_data(self):
        print("class D data")

# obj=D()
# obj.D_data()
# obj.C_frnds()
# obj.B_hello()
# obj.A_hi()
# super() ->  super() method is useful for to access parent class data into te child class

# case -1 :
# we cant access parent class instance vriables from child class directly by using super()
# if we want to access must and should we have ton use self
class A:
    def __init__(self):
        self.a=100  # instance variable
class B(A):
    def hi(self):
        print("parent :",self.a)
        print("Parent :",super(self).a)
# obj=B()
# obj.hi()

# case -2 : we can able to access parent class instance ,static , class method  in child class using super() method inside the instance methhod


class A:
    def A_hi(self):   # instaance
        print("class A hi")
    @classmethod    # class method
    def hello(cls):
        print("A class method ")
    @staticmethod   # static methhod
    def hi_hello():
        print("A static method")

class B(A):
    def python(self): # instnace method
        print("class B instance method")
        super().A_hi()
        super().hello()
        super().hi_hello()
# obj=B()
# obj.python()

# case -3 :   we cant acess parent class instance methods by using super() from child class class method
# we can able to classes parent class staric,class method using super() from child class class method
class A:
    def A_hi(self):   # instaance
        print("class A hi")
    @classmethod    # class method
    def hello(cls):
        print("A class method ")
    @staticmethod   # static methhod
    def hi_hello():
        print("A static method")

class B(A):
    @classmethod
    def python(cls): # instnace method
        print("class B class method")
        #super().A_hi()  #  class A instance method we can not able to access usingg sunper
        super().hello()    # class A class method
        super().hi_hello() # class A static method
# obj=B()
# obj.python()

# case -4 : we r unable to access parent class methods inside the child class static method using super
class A:
    def A_hi(self):   # instaance
        print("class A hi")
    @classmethod    # class method
    def hello(cls):
        print("A class method ")
    @staticmethod   # static methhod
    def hi_hello():
        print("A static method")

class B(A):
    @staticmethod
    def python(): # instnace method
        print("class B class method")
        #super().A_hi()  #  class A instance method we can not able to access usingg sunper
        #super().hello()    # class A class method
        #super(A).hi_hello() # class A static method
        super().A_hi()

B.python()

