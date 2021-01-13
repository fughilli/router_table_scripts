import fractions

def FormatImproper(fract):
    num, den = fract.numerator, fract.denominator
    whole = num // den
    num = num % den
    if whole == 0:
        if num == 0:
            return '0'
        return '{}/{}'.format(num, den)
    if num == 0:
        return '{}'.format(whole)
    return '{} {}/{}'.format(whole, num, den)
