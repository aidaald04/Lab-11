numbers = [15, 30, 45, 12, 5, 90]
divisible_by_15 = filter(lambda x: x % 15 == 0, numbers)

print(list(divisible_by_15))
