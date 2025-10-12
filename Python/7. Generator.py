gen = (x * 2 for x in [1, 2, 3])
print(gen)  # <generator object <genexpr> at 0x...>     s

print(next(gen))  # 2
print(next(gen))  # 4
print(next(gen))  # 6
#print(next(gen))  # StopIteration, once its over there is no more data and  it needs to recreated

for value in gen:
    print(value)  # This won't print anything because the generator is already exhausted]




def contador():
    for i in range(3):
        yield i  # pausa y devuelve un valor

g = contador()
print(next(g))  # 0
print(next(g))  # 1
print(next(g))  # 2
