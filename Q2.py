def count(n):
    counter = 0
    data = []
    for i in range(1, n + 1):
        if (i % 3 == 0 or i % 5 == 0) and (i % 15 != 0):
            continue
        else:
            data.append(i)
            counter += 1
    # print(data)
    return counter


print(count(15))
print(count(30))