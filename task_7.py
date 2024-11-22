sequence = [1, 2, 3, 4, 5]

unique = True
for num in sequence:
    if sequence.count(num) > 1:
        unique = False
        break

print(unique)
