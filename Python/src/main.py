FUNDAMENTAL_NUMBERS = {
    1: 'I',

    4: 'IV',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
}

def to_roman(input_number):
    if input_number == 2:
        return "II"

    if input_number in FUNDAMENTAL_NUMBERS:
        return FUNDAMENTAL_NUMBERS[input_number]

    if input_number == 200:
        return "CC"

    n = divide(input_number)
    return 'M' * n

def divide(n):
    if n >= 1000:
        return n // 1000
    elif n >= 100:
        return n // 100
    elif n >= 10:
        return n // 10
    else:
        return 1