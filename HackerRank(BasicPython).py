n = int(input())
for i in range(n):
    inp = input().split()
    if len(inp) >= 2:
        name = inp[0]
        speed = int(inp[1])
        if len(inp) == 3:
            dis = inp[2]
        if name == 'car':
            print(f'Car with the maximum speed of {speed} {dis}')
        else:
            print(f'Boat with the maximum speed of {speed} knots')
