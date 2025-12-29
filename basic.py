print("1.simple data variable and add operation\n 2. if condition \n 3.Strings")
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
    # area of square
    side = int(input("enter the side:"))
    print(f"side = {side ** 2}")
    #avg of two floating number
    a = float(input("ener fist:"))
    b = float(input("enter second:"))
    print(f"avg = {a+b/2}") 


if choice == 2 :    
    # for if else, nested if else, and elif statements also clever if.
    a = int(input("enter a number:"))
    b = int(input("enter another number:"))
    if a > b :
        print(f"True,{a} is greater then {b}")
        if a % b != 0:
            print(f"{a} is not divisible by {b}")
        else:
            print(f"{a} is divisible by {b}")
    elif a < b:
        print(f"False,{b} is greater than {a}")
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

if choice == 3:
    # for strings
    str1 = "om"
    str2 = 'namah'
    str3 = """Shivaya"""
    str4 = "what's up" #  double quotes if single quote is there in string
    str5 = str1+str2+str3 #omnamahShivaya
    '''use of escape sequence :-
         To give a format to string we use escape sequence
         \n = new line, \t = tab space, \\ = backslash, \' = single quote, \" = double quote'''
    #string concatenation = joining of strings
    # when string is created it is stored in the memory with index value and can only be accessed not modified
    # in calculating length of space the empty spaces' 'are also counted
    print(f"\nfinal string : {str5} length of final string:{len(str5)}")
    # string slicing : to access a particular character in string important for machine learning and it uses index
    # str[starting index : ending index + 1 : step count]
    print(f"\nstring slicing : 1. str5[0:2] = {str5[0:2]} 2. str5[2:] = {str5[2:]} 3. str5[:5] = {str5[:5]} 4. str5[::2] = {str5[::2]} 5. str5[-5:-1] = {str5[-5:-1]} 6. str5[::-1] = {str5[::-1]}")
    # STring functions (str.capitalize function it only display capitalized not change original string)
    print(f"str.endswith = {str5.endswith("aya")}, str5.capitalize = {str5.capitalize()}, str5.replace = {str5.replace("om","hariom")} ") 
