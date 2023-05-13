#abstract is
from abc import ABC,abstractmethod
class test(ABC):
    def method1(self):
        self.d=3
        print("x val is ",self.d)
    @abstractmethod
    def method2(self):
        self.x = 10
        self.y = 20
        print("anji", self.x)
        print("anji", self.y)
        print("anji", self.d)


t=test()
t.method1()
# t.method2()