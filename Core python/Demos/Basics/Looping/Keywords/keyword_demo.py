import keyword 
print(keyword.kwlist)
print(len(keyword.kwlist))

##1. pass:  Neglect the expected indented block error
for i in range(1, 10):
    pass

##2. break:  Terminate the loop
for i in range(1, 5):
    if (i == 3):
        break
    print(i)

##3. continue:  Current iteration wiil be stopped 
for i in range(1, 5):
    if (i == 3):
        continue
    print(i)

##4. else:  Else execute when loop executed successfully
for i in range(1, 5):
    if(i == 8):
        break
    print(i)
else:
    print('Else executed.')
