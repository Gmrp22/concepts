# Crear diccionarios
person = {"name": "Gilda", "age": 25, "city": "Guatemala"}
empty = {}
d2 = dict(name="Juan", age=30)

print(person["name"])  # acceso rápido por clave
print(person.get("age"))  # acceso seguro, devuelve None si no existe   

person = {"name": "Gilda", "age": 25}

# Agregar o modificar
person["city"] = "Guatemala"
person["age"] = 26
person.update({"age": 27, "name": "Gilda Rivera-"})
# Eliminar
del person["city"]
print(person)
removed = person.pop("name")   # devuelve y elimina
print(person)

# Vaciar
copy = person.fromkeys(['name', 'age', 'city'])  # crea un dict con claves dadas y valores None
print(copy, 'copy')
person.clear()

print(len(copy))

person = {"name": "Ana", "age": 22, "city": "NY"}

print(person.keys())    # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['Ana', 22, 'NY'])
print(person.items())   # dict_items([('name','Ana'), ('age',22), ('city','NY')])

# Recorrer
for k, v in person.items():
    print(k, "→", v)


person = {"name": "Ana", "age": 22}
print("name" in person)      # True (busca en claves)
print("Ana" in person)       # False (no busca en valores!)
print(22 in person.values()) # True


#comprehensions
# Crear un dict de cuadrados
squares = {x: x**2 for x in range(5)}
print(squares)

# Filtrar claves
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)

# Invertir claves y valores
original = {"a": 1, "b": 2}
inverted = {v: k for k, v in original.items()}
print(inverted)


students = {
    "Gilda": {"age": 25, "grades": [90, 95, 100]},
    "Juan": {"age": 30, "grades": [80, 85, 88]}
}
print(students["Gilda"]["grades"][0])  # 90
