integers = [10, 15, 22, 33, 45, 51, 27, 12, 55, 2]

for number in integers:
    if number > 50:
        break
    if number % 3 == 0:
        continue
    print(number)