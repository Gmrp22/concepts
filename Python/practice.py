set1 = {1,2,3,4,5}
print(set1)
#set1.remove(10) #error
print(set1)

set1.discard(2) #no error
print(set1)


set2 = {34,(1,3,(34,5)), "hello"}
print(set2)

try:
    set2 = {34,(1,3,[34,5]), "hello"}#error lists are not hashable
    print(set2)
except Exception as e:
    print(e)

array = [1,2,3,4,5,6,7,8,9]
array[1:3] = [9] #can only assign iterable
print(array)


new_tuple = tuple(enumerate(array)) # creates a list of tuples
print(new_tuple)


dic = {'a':1, 'b':2}
print(dic.get("c", "default"))


#sets use values and not index
original = {1,2,3,4,5,(6,7)}
shallow = original.copy()
shallow.add(6)
print(original)
print(shallow)

shallow.remove((6,7))
print(original)
print(shallow)


#shallow copy
array = [1,2, [5,6]]
shallow = array.copy()
print(array)
print(shallow)
shallow[2].append(7)
print(array)
print(shallow)


t = ([1, 2], 3)
t[0].append(99)
print(t)


a,_,b = (10,20,30)
print(a,b)


#update gets an iterable
s = {1, 2, 3}
s.add(2)
s.update([2, 3, 4])
print(s)
