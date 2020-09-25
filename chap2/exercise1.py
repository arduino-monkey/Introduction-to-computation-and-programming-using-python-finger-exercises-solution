def largestOdd(x, y, z):
    odds = [i for i in [x,y,z] if i%2]
    if odds:
        print(max(odds))
    else:
        print('No odd numbers found')


largestOdd(5,6,1)