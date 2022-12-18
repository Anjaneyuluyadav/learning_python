# polymorpism : an entity which represents in multiple forms is caled polyorpism
# Ex : you the best example for polyorpisam ,u r the same but u r actions are defferent based on differnt places
# 1.opertor overloading
# 2.method overloaing
# 3.constructor overloading

# ducktype polymorpisam  : we want to implement same functionly for all the classes but the action is different in diffeent places
class Duck:
    def talk(self):
        print("QUACK QUACK")
class Dog:
    def talk(self):
        print("BOW BOW")
class cat:
    def talk(self):
        print("Moew Moew")
class Goat:
    def talk(self):
        print("Myaah myaah")

# def f1(obj):
#     obj.talk()
# obj=[Duck(),Dog(),cat(),Goat()]
# for object in obj:
#     f1(object)

#hasattribute : hasattribute is method useful for to check whether method exits or not in perticuler object
#synatx :hasattr(object,"method_name")

class Duck:
    def talk(self):
        print("QUACK QUACK")
class Dog:
    def talk(self):
        print("BOW BOW")
class cat:
    def roar(self):
        print("Moew Moew")
class Goat:
    def talk(self):
        print("Myaah myaah")
def f1(obj):
    if hasattr(obj,"talk"):
        obj.talk()
    else:
        obj.roar()


# obj=[Duck(),Dog(),cat(),Goat()] #[obj1,obj2,obj3,obj4]
# for object in obj:
#     f1(object)


# operator overoading : we use same operator for multiple purposess which is nothing but operator overloading

# + ,* already overloaded in python

# a=10
# b=20
# print(a+b)
# c="python"
# d="Java"
# print(c+d)
# # *
# print(a*b)
# c="Hello"
# d=2
# print(c*d)

# + operator oveloading :

# magic methods :
a=10
b=20
print(a.__mul__(b))

# __add__, __sub__,__mul__,__pow__ ,__mod__


#
# class Book:
#     def __init__(self,pages):
#         self.pages=pages
#     def __add__(self,other):
#         return self.pages+other.pages
#     def __sub__(self,other):
#         return self.pages-other.pages
#     def __mul__(self,other):
#         return self.pages*other.pages

# obj1=Book(100)
# obj2=Book(200)
# print(" Total pages :",obj1+obj2) # obj1.__add__(obj2)
# print(" Total pages :",obj1-obj2)
# print(" Total pages :",obj1*obj2)

x=["PYTHON iS GOOD", "JAVA IS GOoD"]   #[OiOOAAIOo]
def python(x):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    out = []
    for i in range(len(x)):
        print(x[i])
        temp = x[i]
        for i in temp:
            if i in vowels:
                out.append(i)
    print(out)
    result = []
    for i in out:
        if i not in result:
            result.append(i)  # [Oi]
    print(result)
python(x)




