def addition(x,y):
    return x + y

def sub(x,y):
    return x - y

def multiply(x,y):
    return x * y

def division(x,y):
    return x / y


num1 = int(input("Enter your first number:"))
num2 = int(input("enter your second number:"))

print("sum is:" , addition(num1 , num2))
print("subtraction is:" , sub(num1 , num2))
print("multiplication is:" , multiply(num1 , num2))
print("division is:" , division(num1 , num2))