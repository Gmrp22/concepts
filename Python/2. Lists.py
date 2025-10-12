import random
colors = ["red", "blue", "green", "yellow"]
#add
colors.append("purple")
colors.insert(len(colors), "extra")
new = colors.__add__(["black", "white"])
colors.extend(["extend", "white"])

print(colors)
print(new)


# remove
colors = ["red", "blue", "green", "yellow", "purple", "extra", "black", "white", "extend", "white"]
colors.pop()
colors.pop(1)
colors.remove("green")
colors.__delitem__(0)
print(colors)
colors.clear()
print(colors)


#modify
colors = ["red", "blue", "green", "yellow", "purple", "extra", "black", "white", "extend", "white"]
colors[0] = "pink"
colors[1:3] = ["orange", "brown"]
print(colors)


#slicing
colors = ["red", "blue", "green", "yellow", "purple", "extra", "black", "white", "extend", "white"]
print(colors[0:3])
print(colors.index("green"))

#other

colors.sort( key= lambda x: len(x))
print(colors,"--")
new = colors.copy()
new.reverse()
counter = new.count("white")
print(new)
print(colors)
print(counter)
len1 = len(colors)

print('pink' in colors)
print('pink' not in colors)
print(colors.__contains__('pink'))

#Compresions
#[ expresión  for elemento in iterable  if condición ]

squares = [x**2 for x in range(10)]
print(squares)

randNumbers = [random.randint(1, 10) for _ in range(10)]
print(randNumbers)

matrix = [[1,2,3], [4,5,6], [7,8,9]]
iterated = [[num for num in row] for row in matrix if sum(row) > 10]
print(iterated, '--')

#Desustructuring
colors = ["red", "blue", "green", "yellow", "purple", "extra", "black", "white", "extend", "white"]
first, second, *rest = colors
print(first)
print(second)
print(rest)

#Itraion

list1 = ["red", "blue", "green"] 
list2= list1*2
print(list2)

print(enumerate(list1))
for index, value in enumerate(list1):
    print(index, value)

new = list(enumerate(list1))
print(new)



lst1 = ["a", "b", "c"]
lst2 = [1, 2]
print(list(zip(lst1, lst2)))




import copy 
print("=== Shallow vs Deep Copy ===")
lst_original = [[1, 2], [3, 4]]
shallow = lst_original.copy()          # shallow copy
deep = copy.deepcopy(lst_original)     # deep copy

shallow[0][0] = 99
print("Original después de shallow:", lst_original)  # Modifica el original
deep[1][0] = 77
print("Original después de deep:", lst_original)     # No afecta el original
print("Deep copy:", deep)

print("\n=== Slicing avanzado con * ===")
colors = ["red", "blue", "green", "yellow", "purple"]
first, *middle, last = colors
print("first:", first)
print("middle:", middle)
print("last:", last)

print("\n=== Comprensión de listas anidadas ===")
nested = [[i,j] for i in range(3) for j in range(2)]
print(nested)
person = [["gilda"], ["juan"], ["ana"]]
age = [23,44,12]
older_person = [[name,newAge**2] for name in person for newAge in age]
print(older_person)


print("\n=== Funciones built-in útiles ===")
numbers = [5, 3, 8, 2, 7]
print("len:", len(numbers))
print("min:", min(numbers))
print("max:", max(numbers))
print("sum:", sum(numbers))
print("reversed:", list(reversed(numbers)))
print("all>0:", all(n > 0 for n in numbers))
print("any>6:", any(n > 6 for n in numbers))


print("\n=== Comprensión con condicional ===")
evens = [x**2 for x in range(10) if x % 2 == 0]
print("Squares of evens:", evens)

print("\n=== Generar números aleatorios ===")
rand_nums = [random.randint(1, 10) for _ in range(5)]
print(rand_nums)