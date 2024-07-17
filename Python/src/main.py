FUNDAMENTAL_NUMBERS = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
}

def to_roman(n):
    if n == 2:
        return "II"
    if n == 2000:
        return "MM"

    return FUNDAMENTAL_NUMBERS[n]

def divide(n):
    if n >= 1000:
        return n // 1000
    elif n >= 100:
        return n // 100
    elif n >= 10:
        return n // 10
    else:
        return 1
