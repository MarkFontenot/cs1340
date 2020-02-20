
try:
    x = 7
    y = 0
    #z = x / y
except ZeroDivisionError:
    print("you can not divide a number by zero")
except NameError:
    print("There is an undefined variable")
else:
    print("everything is fine")


print("this is the next line ")