digits = list(range(1, 51))


# def check_even(number):
# return number % 2 == 0


# ans = list(filter(check_even, digits))
# print(ans)

def jumoke(P):
    return P ** 2


print(list(filter(lambda num: num % 2 == 0, digits)))
print(list(map(jumoke, digits)))
# print(list(map(lambda p: p ** 2, digits)))
