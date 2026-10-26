no = int(input('Enter three digit number = '))

fn = no % 10
no = no // 10

sn = no % 10
no = no // 10

tn = no % 10
no = no // 10

sum = fn + sn + tn

print(f'sum number = ',fn,'+',sn,'+',tn,'= ',sum)