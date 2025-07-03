numb = input("Please input a number: ")
numb2 = input("Please input a second number: ")
oper = input("Please input an operator (+, -, *, /): ")

if oper == "+":
    print(int(numb) + int(numb2) + 0.00)
elif oper == "-":
    print(int(numb) - int(numb2) + 0.00)
elif oper == "*":
    print(int(numb) * int(numb2) + 0.00)
elif oper == "/":
    if numb2 == "0":
        print("Can not divide by zero! ")
    else:
        print( int(numb) / int(numb2) + 0.00)
else:
    print("Invalid operator")
