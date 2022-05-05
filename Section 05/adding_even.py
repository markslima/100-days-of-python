total = 0
also_total = 0
for number in range(1, 101):
    if number % 2 == 0:
      total += number

for number in range (2, 101, 2):
    also_total += number

print(total)

print(also_total)