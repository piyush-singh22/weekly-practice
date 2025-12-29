print("1.simple data variable and add operation\n 2. if condition ")
choice = int(input("enter the number according to what you wish to look:"))
if choice == 1:
    # For data variables  
    var1 = 1
    var2 = 2
    var3 = var1 + var2
    print(var3)
    print(f"subtraction {var2-var1}")
    print(f"multiplication {var2*var3} power {var3 ** var2}")
    print(f"division {var3/var2} floor division {var3//var2}")
    val = True
    val2=True
    val3 = False
    print(f"and operation:{val and val2} or operations: {val or val3} not opperation {not val3}")

if choice == 2 :    
    # for if else, nested if else, and elif statements also clever if.
    a = int(input("enter a number:"))
    b = int(input("enter another number:"))
    if a > b :
        print(f"{a} is greater then {b}")
        if a % b != 0:
            print(f"{a} is not divisible by {b}")
        else:
            print(f"{a} is divisible by {b}")
    elif a < b:
        print(f"{b} is greater than {a}")
        if b % a != 0:
            print(f"{b} is not divisible by {a}")
        else:
            print(f"{b} is divisible by {a}")
    else:
        print("A is equaal to b")
    
    # clever if
    age = int(input("enter age:"))
    vote = ("you can vote", "not eligible to vote ") [age < 18]
    print(vote)

    sal  = int(input("enter your salary:"))
    tax  = sal *(0.2,0.1)[sal<500000]
    print(f"your tax's amount to :{tax}")