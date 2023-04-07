#ASS91) what is class,object,self,init method ?
#
# 2) create a student class print the student data ?
#
class A:
    def stu(self,neme,age,roll):
        self.a=neme
        self.b=age
        self.c=roll
        print("name is:",neme)
        print("stu is age:",age)
        print("stu is:",roll)
    def stu2(self):
        print(self.a)
        print(self.b)
        print(self.c)
# i=A()
# i.stu("anji",22,7)
# i.stu2()
# 3) what are class and instance ,local variables and how to access with examples ?
#class:-->class is collection of fun,mothod ,object
# class is user difined class
class S:
    def test1(self,x,c,v):
        self.a=x
        self.b=c
        self.n=v
        print("result local var:",x)
        print("result local:", c)
        print("result:local var", v)
        print("result instance md:",self.a)
        print("result: instance md", self.b)
        print("result: instance md",self.n)

    def stu(self):
        print(x)
        # print("result:", x)#N/E
        # print("result:", c)#N/E
        # print("result:", v)#N/E
        if self.a>self.b and self.a>self.n and self.b>self.n:
            print("pass")
        else:
            print("fail")

t=S()
t.test1(76,56,54)
t.stu()

# 4) what are the difference b/w method and function ?
#
# 5) what is instance method with exampe ?
#
# 6) what is class method with example ?
#
# 7) what are decorator,generator with example ?
#
# 8) what are reduce,map,filter functions with examples ?
#
# 9) crete a function that accepts string as a parameter and returns dict from fun
#   # count all alphabets,vowels,consonents,numbers and specialchar and store in dict and return the dict
#   # ex : "He#44AaB$"  op ={alpha:5,num:2,vowels:3,conso:2,spec:2}
#
# 10) x=[1,4,3,10] print the binary format each element of list op:['0001','0100','0011','1010']
#
# 11) write  example of intance,static,class method with rules?
#
# 12) how to access one class data into another class without using inheritance ?
#
# 13) what is inheritance ? how many types of inheritances are there with example ?
#
# 14) what to access super class data from child class using super method ?
#
# 15) what is function overloding and operator overoading with example?