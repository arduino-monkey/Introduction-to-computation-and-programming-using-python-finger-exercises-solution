def largestOdd(lis):
    odds = [i for i in lis if i%2]
    if odds:
        print(max(odds))
    else:
        print('No odd numbers found')


numbers = []
for i in range(10):
    x = int(input('Enter interger: '))
    numbers.append(x)


largestOdd(numbers)
