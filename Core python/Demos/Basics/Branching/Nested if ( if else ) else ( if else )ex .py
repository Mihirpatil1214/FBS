gender = input('Enter gender (Male /Female)= ')
age = int(input('Enter age = '))

if (gender == 'Male'):
    if (age >= 21):
        print(f'Boy is eligible for marriage.')
    else:
        print(f'Not eligible.')
else:
    if(age >= 18):
        print(f'girl is eligible for marriage.')
    else:
        print(f'Not eligible.')
