days = int(input('Days = '))

years = days // 365

remainder_days = days % 365

weeks = remainder_days // 7

remainder_week_days = remainder_days % 7

print(f'days to years =',years,'remainder days =',remainder_days)
print(f'remainder days to weeks =',weeks,'remainder week days =',remainder_week_days)