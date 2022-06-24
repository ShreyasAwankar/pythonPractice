import Main1

print ("If the substract function  is not put inside ",
           "the 'if __name__==__main__' then it would also execute in this file ",
           "if we imoprt this (Main1) in this file even if we dont call it... ", "\n")

a = int(input("a = ? \n"))
b = int(input("b = ? \n"))

print (Main1.add(a,b), "\n")
print (Main1.multiply(a,b))