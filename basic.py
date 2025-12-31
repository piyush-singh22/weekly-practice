print("1.simple data variable and add operation\n 2. if condition \n 3.Strings \n 4.Lists \n 5.Tuples")
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
    # for if else, nested if else, and elif statements also clever if conditional .
    a = int(input("enter a number:"))
    b = int(input("enter another number:"))
    c = int(input("enter third number:"))
    if a > b and a > c:
        print(f"True,{a} is greater then {b}")
        if a % b != 0 or a % 2 == 0:
            print(f"{a} is not divisible by {b} but is even number")
        else:
            print(f"{a} is divisible by {b}")
    elif b > a and b > c:
        print(f"False,{b} is greater than {a} and {c}")
        if b % a != 0:
            print(f"{b} is not divisible by {a}")
        else:
            print(f"{b} is divisible by {a}")
    else:
        print("c is greater")
    
    # to check multiple 
    if(a%2==0):
        print(f"{a} is multiple of 2")

    # clever if
    age = int(input("enter age:"))
    vote = ("you can vote", "not eligible to vote ") [age < 18] # in cleverif the first value is for false condition and second for true condition
    print(vote)

    sal  = int(input("enter your salary:"))
    tax  = sal *(0.2,0.1)[sal<500000]
    print(f"your tax's amount to :{tax}")

    

if choice == 3:
    # for strings
    str1 = "om"
    str2 = 'namah'
    str3 = """Shivaya"""
    str4 = input("enter a first name:") #  double quotes if single quote is there in string
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
    # (str.find function returns -1 if not found and if found then give the index value)
    print(f"str.endswith = {str5.endswith("aya")}, str5.capitalize = {str5.capitalize()}, str5.replace = {str5.replace("om","hariom")}, str5.find = {str5.find("namah")}, str5.lower = {str5.lower()}, str5.upper = {str5.upper()} str5.count = {str5.count('a')}")
    print(f"len of name: {len(str4)}-name is {str4}")
    print(f"occurance of '$' in str4 : {str4.count('$')}")
if choice == 4:
    #for lists = mutable (can be changed) ordered collection of items built in data type
    list1 = ["piyush",90,20, "Surat"]
    #list slicing : list1[starting index : ending index + 1 : step count] same as string slicing ending index is not included
    print(f"list slicing : 1. list1[1:3] = {list1[1:3]}")
    # list methods:- list.append(), list.insert(index,value), list.remove(value), list.pop(index), list.sort(), list.reverse(), list.count(value), list.extend(another list)
    list2 = [1,2,3,4,5]
    list2.append(6)
    list2.insert(0,0)
    # if print(list2.remove(3)): it gives error as it returns None same for list2.sort() and list2.append()
    list2.sort()
    print(list2)
    list2.reverse()
    print(f"reversed list2: {list2}")
    # list.remove removes first occurance of value and list.pop removes value at index and returns it
    list2.remove(5)
    print(f"after removing 5: {list2}") 
    # problem 1
    movies = list(input("enter 3 movie names seperated by comma :").split(','))
    print(f"movies list : {movies}")
    # problem 2
    list1 = [1,2,3,2,1]
    list2 = list1.copy()
    list2.reverse()
    decision = ("no","yes")[list1 == list2]
    print(f"palandrome check : {decision}")
    print(f"reversed list : {list2}")
    print(f"original list : {list1}")

if choice == 5:
    #for tuples = immutable (cannot be changed) ordered collection of items built in data type () parenthesis used to define tuple
    tuple1 = ("piyush",90,20, "Surat")
    # in tuple if we place a single value it is considered as string or int so to define single value tuple we use comma after value
    tuple2 = (1,)
    print(tuple2)
    #tuple slicing : tuple1[starting index : ending index + 1 : step count] same as string slicing ending index is not included
    print(f"tuple slicing : 1. tuple1[1:3] = {tuple1[1:3]}")
    # tuple methods:- tuple.count(value), tuple.index(value)
    print(f"occurance of 20 in tuple1: {tuple1.count(20)} at index: {tuple1.index(20)}")
    # problem 1
    tup = ("c","D","A","A","B","B","A")
    count_A = tup.count('A')
    print(f"no of student got grade A is :{count_A}")