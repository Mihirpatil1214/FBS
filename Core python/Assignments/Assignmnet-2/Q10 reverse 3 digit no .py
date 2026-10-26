no = int(input('Enter three digit number = '))
#321

fn = no % 10
no = no // 10

sn = no % 10
no = no // 10

tn = no % 10
no = no // 10

print(f'Reverse number = ',fn,sn,tn)
