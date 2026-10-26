x = 10   # immutable 
y = 10   # Reuse

li1 = [10, 20]    # Mutable
li2 = [10, 20]    # can't reuse


#1. is           # doghanch memory location same aslya tar 'true' print karel
               
print(x is y)

print(id(x))
print(id(y))

print(li1 is li2)

print(id(li1))
print(id(li2))


# not is      # doghanch memory location same nasel tar 'true' print karel
