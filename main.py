def multiply(n):
    while n > 9:
        digits = [int(digit) for digit in str(n)]
        product = 1
        for digit in digits:
            product *= digit
        n = product
    return n

number = int(input("Введіть число: "))
result = multiply(number)
print(result)
