def division(a, b):
    try:
        res = a/b
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except TypeError:
        print("TypeError")
    else

print(division(1, ''))
