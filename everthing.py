import re
class myFirstclasss():
    def myMethod(self):
        print("Soryy")
    def myMethos2(self):
        print("Thank you")
class myclass(myFirstclasss):
    def mymethod3(self):
        print("lovely")
c = myclass
#c.myMethod()
#c.myMethos2()
#c.mymethod3()
rx = "I love my family.I am blessed to have such amazing family"
print(re.split(r" ",rx))
