n = int(input('Emter number = '))

for i in range(2, n):
    if(n % i == 0):
        print(n,'Not prime number.')
        break
else:
    print(n, 'Prime number.')