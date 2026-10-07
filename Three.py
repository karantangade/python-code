print("Enter 1 for add");
print("Enter 2 for divi");
choice=int(input("Enter the choice"));
a=int(input("Enter the frist number"));
b=int(input("Enter the second number"));

match choice:
    case 1:
        print("addition is",a+b);
    case 2:
        print("divi is ", a//b);
    case _:
        print("Enter valiad input");
