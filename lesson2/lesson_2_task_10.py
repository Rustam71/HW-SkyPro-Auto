
def bank(x, y):
    balance = x
    for mos in range(y):
        balance = balance * 1.1
    return balance

print(bank(1000, 5))