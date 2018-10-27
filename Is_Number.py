def is_number(n):
    flag = True
    try:
        num = float(n)
        flag = num == num
    except ValueError:
        flag = False
    return flag
