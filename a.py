class withs ():
    def __init__(self,name):
        self.name = name 
        print(name)
class A (withs):
    def __init__(self):
        print("你是伞兵吗")
class B(withs):
    def __init__(self, name):
        super().__init__(name)
class AB (A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self,123)
        print("我是伞兵")
a = AB()
print(a)
    
    