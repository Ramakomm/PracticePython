class A:
    def __init__(self,v1,v2):
        self.cpu = v1
        self.ram = v2
        print("trying")
    def desc(self):
        print("First classs")
cool = A(45,58)
cool.desc()
print(cool.cpu,cool.ram)
