print("1 addition")
print("2 multiply")
print("3 subtraction")
print("4 division")

num1 = float(input("enter num1 :"))
formular =(input("Enter formular :"))
num2 = float(input("enter num2 :"))

if formular == "1":
    print(num1 + num2)
elif formular == "2":
    print(num1*num2)
elif formular == "3":
    print(num1-num2)
elif formular == "4":
    if num2 == 0:
        print("maths error")
    else:
        print(num1/num2);




