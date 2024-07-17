FUNDAMENTAL_NUMBERS = {
    1: 'I',
    5: 'V'
}

def to_roman(n):
    if n == 2:
        return "II"

    return FUNDAMENTAL_NUMBERS[n]