p = int(input('principal amount = '))
r = int(input('rate of intrest = '))
t = int(input('time in years = '))

compound_intrest = p*(1+(r/100))**t

print(f'compund intrest =',compound_intrest)