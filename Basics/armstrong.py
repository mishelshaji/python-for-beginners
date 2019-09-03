# ARMSTRONG
num = int(input('Enter the maximum limit'))

for i in range(0, num + 1):
    # Finding the number of digits
    temp = i
    count = 0
    while temp > 0:
        count += 1
        temp = temp // 10
    # print(f'Count: {count}')

    temp = i
    total = 0
    while temp > 0:
        e = temp % 10
        total = total + (e ** count)
        temp = temp // 10
    # print(total)
    if total == i:
        print(total)
