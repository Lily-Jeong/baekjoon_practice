one, two, three = map(int, input().split())
if one == two == three:
    prize = 10000 + (one * 1000)
elif one == two:
    prize = 1000 + (one * 100)
elif two == three:
    prize = 1000 + (two * 100)
elif one == three:
    prize = 1000 + (one * 100)
else:
    prize = (100 * max(one, two, three))
print(prize)