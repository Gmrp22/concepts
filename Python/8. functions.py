
#args with names
def printS(a,b):
    print('a =',a,', b =',b)

printS(b=2,a=1)


#default values, always at the end
def printS1(a,b=2):
    print('a =',a,', b =',b)
#saves in a tuple
def printS2(*a):
    print('a =',a)
          
printS2(1,2,3,4,5)

#saves in a dictionary
def printS3(**a):
    print('a =',a)

printS3(a=1,b=2,c=3,d=4,e=5)


#ORDER
#Parámetros normales

#*args

#Parámetros con nombre (opcionales)

#**kwargs

def printS4(a,*c,d=4,**e):
    print('a =',a) # 1
    print('c =',c) # (2,3,5,6)
    print('d =',d)# 7
    print('e =',e) # {'g': 8}

printS4(1,2,3,5,6,d=7,g=8)


#inversed destructuring
def printS5(a,b,c):
    print('a =',a)
    print('b =',b)
    print('c =',c)

t = (1,2,3)
printS5(*t)

info = {"a": 10, "b": 20, "c": 30}
printS5(**info)



# ------------------ Reference vs Value ------------------


#---- By reference, lists, dictionaries, sets are passed by reference, meaning changes made to the object within the function will be reflected outside the function as well.

#--- [] as default value, the list is initialized only once, whebn the function is defined --important
def modify_list(lst =[]):
    lst.append(4)
    print("Inside function:", lst)
    return lst

lst = modify_list()
modify_list()  # The list retains its state between calls
modify_list(lst)  # returns same list
print("Outside function:", modify_list())  # Shows the same list

#since we are reasigning the list, it does not retain its state
def modfy_list2(lst = None):
    if lst is None:
        lst = []
    lst.append(1)
    print("Inside function:", lst)
    return lst
lst = modfy_list2()
modfy_list2()  # The list does not retain its state between calls
modfy_list2(lst)  # A new list is created
print("Outside function:", modfy_list2())  # Shows the modified list


#----- By value, numbers, strings, tuples are passed by value
def modify_number(num):
    num += 10
    print("Inside function:", num)
    return num

number = 5
modify_number(number)  # The original number remains unchanged
print("Outside function:", number)  # Shows the original number
modify_number(20)  # Works with a new number
modify_number(number)  # Again, original number remains unchanged
print("Outside function:", number)  # Still shows the original number




