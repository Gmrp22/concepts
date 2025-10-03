# Crear sets
s1 = {1, 2, 3}
s2 = set([2, 3, 4])
s_empty = set()  # set vacío, {} sería un dict

# Sets pueden contener cualquier tipo inmutable
s_mixed = {1, "hello", (2,3)}
s = {1, 2, 3}

# Añadir elementos
s.add(4)
s.update([5,6,7,8])  # añade múltiples

# Eliminar elementos
s.remove(2)  # error si no existe
print(s)
s.discard(10)  # no da error si no existe

elemnt= s.pop()        # elimina primer elemento

print(elemnt, '--', s)
s.clear()      # vacía el set

print(s)


a = {1,2,3,4}
b = {3,4,5,6}

print(a.union(b))          # {1,2,3,4,5,6} → todos los elementos
print(a.intersection(b))   # {3,4} → elementos en común
print(a.difference(b))     # {1,2} → en a pero no en b
print(a.symmetric_difference(b))  # {1,2,5,6} → en a o b, no en ambos


s = {1,2,3}
print(1 in s)   # True
print(4 not in s) # True


s = {1,2,3}
for val in s:
    print(val)

# Enumerate también funciona, pero el orden no es garantizado
for i, val in enumerate(s):
    print(i, val)


# Crear set de cuadrados de 0 a 9
squares = {x**2 for x in range(10)}
print(squares)

# Filtrar elementos
evens = {x for x in range(10) if x % 2 == 0}
print(evens)
