
list = []
for number in range(1, 50):
    list.append(number)

for item in list:
    if item == 13:
        continue
    elif item == 39:
        break
    else:
        print(item)
