class Withtest():
    def __init__(self,name):
        self.name = name
        pass
    def __enter__(self):
        print("sanco")
        return self
    def __exit__(self,type,value,trace):
        print("type",type)
        print("cnsk")
    def play(self):
        print("now,i am playing")
        print(1/0)
with Withtest("coai") as t:
    t.play()

