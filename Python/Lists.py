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
len = len(colors)

print('pink' in colors)
print('pink' not in colors)
