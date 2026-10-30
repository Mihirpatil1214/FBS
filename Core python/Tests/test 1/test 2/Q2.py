num = int(input('Enter three digit number = '))

d1 = num % 10
num = num // 10

d2 = num % 10
num = num // 10

d3 = num % 10 
num = num // 10

fn = d3 // 2
tn = d3 * 2

if (fn == d2) and (tn == d1):
    print('yes you have done it.')
else:
    print('please try next time.')
