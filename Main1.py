"""It is not necessary in this programme but it is a good practise to use it after we write all
functions in a programme. Advance programmers import the functions many times in many other
programmes too in that case the part of the code where the functions are being called must be
kept in if name == 'main' so that those parts don't get called along with functions
Give a like if you like it"""
print (f"the name of the file is  {__name__} \n")
def add(a,b):
    return f"Sum = {a+b}"

def multiply(a,b):
    return f"Multipliction = {a*b}"


if __name__ == '__main__':
    a= int(input("Enter a"+'\n'))
    b =int(input("Enter b"+'\n'))
    def substract(a,b):
        return f"Substraction = {a-b}"

    print(add(a,b))

    print (substract(a,b),'\n')
    print (multiply(a,b))


