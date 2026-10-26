area = float(input('Enter area of one wall ='))
interior_rate = float(input('Enter interior panting rate = '))
exterior_rate = float(input('Enter exterior panting rate = '))

number_of_walls = 8

total_area = area * number_of_walls

interior_cost = total_area * interior_rate
exterior_cost = total_area * exterior_rate 

total_cost = interior_cost + exterior_cost

print(f'Interior painting cost = ',interior_cost)
print(f'Exterior painting cost = ',exterior_cost)
print(f'Total painting cost = ',total_cost)
