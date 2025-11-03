
[a,b] = [1,2]
print(a)

a,b = [3,4]
print(a)


dictionary = {"a":"testA", "b": "testB", "c": "testC"}

a,_,b = dictionary.values()
print(a)

a, *rest = dictionary
print(rest)


def args(*args):
    print(args)

#returns tuple
args(1,2,3,4,5)

#inverse operation

def args(a,b,c):
    print("a", a)
    print("b",b)
    print("c",c)

args(*[1,2,3])


#kwargs

def kwargs(a,b,**restOfThem):
    print(restOfThem)

kwargs(1,2,{"a":1,"b":2})