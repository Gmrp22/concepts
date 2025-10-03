# Definición de tuplas
t = (1, 2, 3)
t2 = 4, 5, 6  # también válido
t_empty = ()
t_single = (1,)  # tupla de un solo elemento, la coma es obligatoria

# Tuplas anidadas
nested = (1, (2, 3), 4)


#Slicing
t = (10, 20, 30, 40, 50)

print(t[0])    # 10
print(t[-1])   # 50
print(t[1:4])  # (20, 30, 40)


#Operaciones basicas
t1 = (1, 2)
t2 = (3, 4)

# Concatenar
t3 = t1 + t2
print(t3)  # (1, 2, 3, 4)

# Repetir
print(t1 * 3)  # (1, 2, 1, 2, 1, 2)
tuple2 = (1, 2, 3)*3
print(tuple2)
# Longitud
print(len(t3))  # 4

# Pertenencia
print(2 in t3)   # True
print(5 not in t3)  # True

#metodos
t = (1, 2, 3, 2, 4)
print(t.count(2))  # 2
print(t.index(3))  # 2

# Desempaquetado
t = (10, 20, 30, 40)

a, b, c, d = t
print(a, b, c, d)  # 10 20 30 40

# Usando *
first, *middle, last = t
print(first)   # 10
print(middle)  # [20, 30]
print(last)    # 40


t1 = (1, 2, 3)
t2 = (4, 5, 6)

# Enumerate
for i, val in enumerate(t1):
    print(i, val)
print("-----zip")
# Zip
for a, b in zip(t1, t2):
    print(a, b)

t3 = list(enumerate(t2))
print(t3)


#nested comprehension
nested = ((1,2), (3,4))
flattened = tuple(x for pair in nested for x in pair)
print(flattened)  # (1, 2, 3, 4)


index = (1, 2, 3, 4, 5)
numbers = (1, 2, 3, 4, 5)
squared = tuple([x**2, i] for x in numbers for i in index if i % 2 == 0)
print(squared)  # (100, 400, 900, 1600,