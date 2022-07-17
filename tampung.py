x = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def romantoint(s):
    tampung = 0
    for a in s:
        if a == 'I':
            tampung = tampung + 1
        if a == 'V':
            tampung = tampung + 5
        if a == 'X':
            tampung = tampung + 10
        if a == 'L':
            tampung = tampung + 50
        if a == 'C':
            tampung = tampung + 100
        if a == 'D':
            tampung = tampung + 500
        if a == 'M':
            tampung = tampung + 1000
    return tampung


s = "II"
print(romantoint(s))
