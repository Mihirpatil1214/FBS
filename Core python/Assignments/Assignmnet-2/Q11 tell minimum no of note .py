amount = int(input('Enter rs = '))

a = amount // 500
b = amount % 500

c = b // 200
d = b % 200

e = d // 100
f = d % 100

g = f // 50
h = f % 50

j = h // 20
k = h % 20

l = k // 10
m = k % 10

print(f'total number of note = ',a + c + e + g + j + l)


