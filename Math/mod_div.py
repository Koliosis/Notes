

def mod_div(a, b, c=1):
    counter = 0
    a = a ** c
    if a > 0:
        while a > b:
            a -= b
            counter += 1
    else:
        while a < 0:
            a += b
            counter += 1
    return a, f'counter = {counter}'

print(mod_div(7, 26, 1001))
