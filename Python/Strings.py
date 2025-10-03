##Print something
name = 'Gilda'
age = 36
print(name, str(age))
print(name + str(age))
print(f'my name is {name} my age is {age})')
print('my name is {} my age is {}'.format(name,age))
print("Hola {nombre}, tienes {edad} años".format(nombre="Gilda", edad=25))


format = lambda name,age : name + str(age)
print(format('Gilda',24))

#methods
'''
Manipulación básica

str.lower() → convierte todo a minúsculas.

str.upper() → convierte todo a mayúsculas.

str.capitalize() → primera letra en mayúscula, el resto en minúscula.

str.title() → pone en mayúscula la primera letra de cada palabra.

str.swapcase() → invierte mayúsculas/minúsculas.
'''
messages = "   Hello, welcome to the world of Python programming!   "
lower=messages.lower()
print(lower)
print(messages.upper())
print(messages.capitalize())
print(messages.title())
print(messages.swapcase())

'''
Quitar espacios o caracteres

str.strip() → elimina espacios (u otros caracteres) al inicio y fin.

str.lstrip() → elimina a la izquierda.

str.rstrip() → elimina a la derecha.

'''
messages = "   Hello, welcome to the world of Python programming!   "
print(messages.strip())
print(messages.lstrip())
print(messages.rstrip())

'''

Búsqueda

str.find(sub) → índice de la primera aparición, o -1 si no está.

str.index(sub) → como find, pero da error si no encuentra.

str.rfind(sub) → índice de la última aparición.

str.count(sub) → cuántas veces aparece un substring.

str.startswith(prefix) → True si empieza con.

str.endswith(suffix) → True si termina con.

'''
messages = "sHello, welcome to the world of Python programming!   "
print(messages.find("welcome"))
print(messages.index("welcome"))
print(messages.rfind("S"))
print(messages.count("o"))
print(messages.startswith("sH"))
print(messages.endswith("g!   "))

'''
 Reemplazo y división

str.replace(old, new) → reemplaza ocurrencias.

str.split(sep) → divide en lista usando un separador.

str.rsplit(sep) → divide desde la derecha.

str.splitlines() → divide por saltos de línea.

str.join(iterable) → une elementos de un iterable con el string como separador.

'''
messages = "Hello, welcome to the world of Python programming!   "
print(messages.replace("o","0"))
print(messages.split(" "))
print(messages.rsplit(" ",3))
multi_line = "First line.\nSecond line.\nThird line."
print(multi_line.splitlines())
words = ["Hello", "world", "in", "Python"]
print(" ".join(words))
'''
 Formato y alineación

str.center(width) → centra con espacios.

str.ljust(width) → alinea a la izquierda.

str.rjust(width) → alinea a la derecha.

str.zfill(width) → rellena con ceros a la izquierda.

✅ Chequeos lógicos

str.isalpha() → solo letras.

str.isdigit() → solo dígitos.

str.isalnum() → letras o dígitos.

str.isspace() → solo espacios.

str.islower() → todo minúscula.

str.isupper() → todo mayúscula.

str.istitle() → estilo título.

 Otros útiles

str.encode() → codifica a bytes.

str.format() → formato estilo plantilla.

str.removeprefix(x) → quita un prefijo si existe (Python 3.9+).

str.removesuffix(x) → quita un sufijo si existe (Python 3.9+).
'''



# Escpae and unicode
# Normal
print("C:\\nueva_carpeta\\archivo.txt")
# Raw string
print(r"C:\nueva_carpeta\archivo.txt")

print("Hola\nMundo")   # salto de línea
print("Tab\tSeparado") # tabulación
print("Comillas: \"hola\"") # comillas dentro del string

#siempre 3
text = "hello-world-python"
print(text.partition("-"))   # ('hello', '-', 'world-python')
print(text.rpartition("-"))  # ('hello-world', '-', 'python')
