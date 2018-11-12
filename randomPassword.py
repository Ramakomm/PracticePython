import string
import random
def randomPasswordGenerator():
    lCase = "abcdefghijklmnopqrstuvwxyz"
    uCase = "ABCDEFGHIJKALMNOPQRSTUVWXYZ"
    digits='0123456789'
    splChar = "@#&*^%$"
    password = ""
    password += random.choice(uCase)
    password += random.choice(lCase)
    password += random.choice(digits)
    password += random.choice(splChar)
    password += random.choice(uCase)
    password += random.choice(lCase)
    password += random.choice(digits)
    print(password)
#randomPasswordGenerator()
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
p =  "".join(random.sample(s,passlen ))
print(p)
