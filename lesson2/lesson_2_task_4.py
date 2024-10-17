n = 30

for fizz_buzz in range(1, n):
    if fizz_buzz % 3 == 0:
        print('Fizz')
    else:
        if fizz_buzz % 5 == 0:
            print('Buzz')
        else:
            if fizz_buzz % 3 == 0 and fizz_buzz % 5 == 0:
                print('FizzBuzz')
            else:
                print(fizz_buzz)
