#calculator
print("+ = addition")
print("- = subraction")
print("* = multiplication")
print("/ = division")
print("** = exponent")
print("% = remainder")

A=int(input("enter number 1 ="))
B=int(input("enter number 2 ="))
choose=(input("choose an operation ="))

if(choose == '+'):
    result = A + B
elif(choose == '-'):
    result = A - B
elif(choose == '*'):
    result = A * B
elif(choose == '/'):
    result = A / B
elif(choose == '**'):
    result = A ** B
elif(choose == '%'):
    result = A % B
else:
    print("invalid operation is given")

print("result =",result)
