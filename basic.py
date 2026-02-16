print("1.simple data variable and add operation\n 2. if condition \n 3.Strings \n 4.Lists \n 5.Tuples \n 6.Dictionaries \n 7. Sets \n 8. Loops \n 9. Functions")
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
    print(f"\n str.endswith = {str5.endswith("aya")}, str5.capitalize = {str5.capitalize()}, str5.replace = {str5.replace("om","hariom")}, str5.find = {str5.find("namah")}, str5.lower = {str5.lower()}, str5.upper = {str5.upper()} str5.count = {str5.count('a')}")
    print(f"\n len of name: {len(str4)}-name is {str4}")
    print(f"\n occurance of '$' in str4 : {str4.count('$')}")
if choice == 4:
    #for lists = mutable (can be changed) ordered collection of items built in data type
    list1 = ["piyush",90,20, "Surat"]
    #list slicing : list1[starting index : ending index + 1 : step count] same as string slicing ending index is not included
    print(f"\n list slicing : 1. list1[1:3] = {list1[1:3]}")
    # list methods:- list.append(), list.insert(index,value), list.remove(value), list.pop(index), list.sort(), list.reverse(), list.count(value), list.extend(another list)
    list2 = [1,2,3,4,5]
    list2.append(6)
    list2.insert(0,0)
    # if print(list2.remove(3)): it gives error as it returns None same for list2.sort() and list2.append()
    list2.sort()
    print(list2)
    list2.reverse()
    print(f"\n reversed list2: {list2}")
    # list.remove removes first occurance of value and list.pop removes value at index and returns it
    list2.remove(5)
    print(f"\n after removing 5: {list2}") 
    # problem 1
    movies = list(input("enter 3 movie names seperated by comma :").split(','))
    print(f"\n movies list : {movies}")
    # problem 2
    list1 = [1,2,3,2,1]
    list2 = list1.copy()
    list2.reverse()
    decision = ("no","yes")[list1 == list2]
    print(f"\n palandrome check : {decision}")
    print(f"\n reversed list : {list2}")
    print(f"\n original list : {list1}")

if choice == 5:
    #for tuples = immutable (cannot be changed) ordered collection of items built in data type () parenthesis used to define tuple
    tuple1 = ("piyush",90,20, "Surat")
    # in tuple if we place a single value it is considered as string or int so to define single value tuple we use comma after value
    tuple2 = (1,)
    print(tuple2)
    #tuple slicing : tuple1[starting index : ending index + 1 : step count] same as string slicing ending index is not included
    print(f"\n tuple slicing : 1. tuple1[1:3] = {tuple1[1:3]}")
    # tuple methods:- tuple.count(value), tuple.index(value)
    print(f"\n occurance of 20 in tuple1: {tuple1.count(20)} at index: {tuple1.index(20)}")
    # problem 1
    tup = ("c","D","A","A","B","B","A")
    count_A = tup.count('A')
    print(f"\n no of student got grade A is :{count_A}")
if choice == 6:
    # for dictionaries = unordered , mutable (can be changed) & don't allow duplicates keys also it is used to store data in key:value pair within {} curly braces AND IS BUILT in data type
    #  dictionary methods:- dict.keys() - returns keys, dict.values() - return values, dict.items() - returns key-value pairs, dict.get(key) - , dict.update({key:value}), dict.pop(key), dict.clear()
    # in dictionary the keys can be float, int , bool, strings, tuple and for values any data type can be used including list
    dict = {"name":"piyush","cgpa":8.86,"marks":[98,95,90]}
    dict["spi"] = 9.0 # to add new key value pair
    print(f"\n dictionaries :- {dict}")
    # nested dictionary
    nested_dict = {"name":"piyush", "subjects": {"maths":83,"phy":90,"bio":98},"percentage":95}
    print(f"\n to access nested dictionary value or modify it : {nested_dict["subjects"]["maths"]}")
    print(f"\n length of dictionary : {len(nested_dict)} and length along with type casting : {len(list(nested_dict.keys()))}")
    pairs = list(nested_dict.items())
    print(f"\n dictionary methods dict.value():{nested_dict.values()}, accessing nested_dict through index pairs[0] : {pairs[0]}")
    #both normal and dict.get(key)methods return value but then why needed dict.get() method because if key is not present in dictionary then it returns None instead of error
    #thus if encounterd error the program will not stop abruptly and continue executing further statements and if used normal method it will give error and stop executing further statements
    print(f"\n normal method : {nested_dict["name"]} and dict.get() method : {nested_dict.get("name")}")
    nested_dict.update({"city":"Surat", "age":20})
    print(f"\n after updating nested_dict.update() = {nested_dict}")
    # problem 1
    practice_question = {"table":["a piece of furniture", "list of facts and figures"], "cat":"a small animal"}
    print(f"\n solution to practice question : {practice_question}")
    # problem 2
    # WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
    # an empty dictionary & add one by one. Use subject name as key & marks as value.
    marks = list(input("enter marks of 3 subjects seperated by space OR comma:").split(' '))
    empty_dict = {}
    subjects = ['maths', 'bio', 'phy']
    for i in range (3):
        empty_dict[subjects[i]] = marks[i]
    print(empty_dict)

    print(f"approach taken by apnacollege :-")
    marks = {}

    x = int(input("enter phy : "))
    marks.update({"phy" : x})

    x = int(input("enter math : "))
    marks.update({"math" : x})

    x = int(input("enter chem : ") )
    marks.update({"chem" : x})

    print(marks)


if choice == 7:
    # for sets is unordered, mutable and each element is unique (duplicate or more than one will not be counted) and immutable(can not be changed) it can only not store dictonary and list
    # sets is case sensitive as if there are two values 'a' and 'A' (or 'cat' and 'Cat') then both will be counted as unique values
    set1 = {1,2,3,4,5,5,4}
    set2 = {1,2,"piyush", True, 2.4}
    #sets will ignore duplicate values and store only unique values as it will not count duplicate values
    print(f"\n sets :- {set1} set2 :- {set2} length of set1 : {len(set1)} and length of set2 : {len(set2)}")
    empty_set = set() # to define empty set
    print(f"\n empty set : {empty_set} type of empty set : {type(empty_set)}")
    # set methods:- set.add(value), set.remove(value), set.pop(), set.union(another set), set.intersection(another set), set.difference(another set), set.clear()
    empty_set.add(1)
    empty_set.add(2)
    empty_set.add(2)
    empty_set.add(3)
    empty_set.add(3)
    print(f"\n used set.add() method to add values in empty set : {empty_set}")
    empty_set.remove(2)
    print(f"\n used set.remove() method to remove value 2 from empty set : {empty_set}")
    set1.clear()
    print(f"\n used set.clear() method to clear all values from set1 : {len(set1)}")
    print(f"\n set.pop() method removes and returns an arbitrary value from the set : popped value : {set2.pop()} and set2 after popping : {set2}")
    # set methods union - returns a new set with all elements from both sets, intersection - returns a new set with common elements, difference - returns a new set with elements in first set but not in second
    print(f"\n set's union method of set2 and empty_set : {set2.union(empty_set)}")
    print(f"\n set's intersection method of set2 and empty_set : {set2.intersection(empty_set)}")
    print(f"\n set's difference method of set2 and empty_set : {set2.difference(empty_set)}")
    # problem 1
    #  You are given a list of subjects for     students. Assume one classroom is required for 1
    # subject. How many classrooms are needed by all students.
    # "python", "java", "C++", "python", "javascript",
    # "java", "python", "java", "C++", "C"
    classrooms = {"python", "java", "C++", "python", "javascript","java", "python", "java", "C++", "C"}
    print(f"\n no of classrooms needed is equal to no of unique subjects : {len(classrooms)}")
    # problem 2
    set = {9, '9.0'} 
    set_tup = {("float", 9.0), ("int", 9)}
    print(f"solution :- {set} and other approach through tuples :- {set_tup }")

if choice == 8:
    # for loops 
    # there should not be any infinite loop 
    print(f"solution :")
    i=1
    while i<101:
        print(i)
        i += 1
    while i>1:
        print(i)
        i-=1    
    a = int(input("enter a number for multiplication"))
    while i<11:
        print(f"{a} * {i} = {a*i}")
        i+=1
    l = [1,4,9,16,25,36,49,64,81,100]
    i=0

    while i < len(l):
        print(l[i])
        i+=1
    
    l = (1,4,9,16,25,36,49,64,81,100)
    i=0
    while i<len(l):
        
        if l[i] == 81:
            print(f"it is at {i+1} index")
    
        i+=1
    print("solution : sum of n number")
    a = int(input("enter a number"))
    i=0
    sum=0
    while i<=a:
        sum+=i
        i+=1
    print(f"value of sum:{sum}")
    print("solution : factorial")
    a = int(input("enter a number"))
    i=0
    fact=0
    while i<=a:
        sum*=i
        i+=1
    print(f"value of sum:{fact}")

if choice == 9 :
    #function is block of code it is used to decrease the code redundancy and increase the reusability of code and it is defined by def keyword
    def add(a,b):
        sum = a+b
        return sum
    a = add(5,8)
    print(a)