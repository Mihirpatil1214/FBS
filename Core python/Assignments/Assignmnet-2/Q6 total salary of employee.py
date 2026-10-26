salary = int(input('Employee salary = '))

da = salary * 10 / 100
ta = salary * 12 / 100
hra = salary * 15 / 100

total_salary = salary + da + ta + hra

print(f'total salary of employee = ',total_salary)