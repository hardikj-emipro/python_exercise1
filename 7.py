while True:
    s=input('Enter non negative integer number')
    if s.isdigit() and int(s) >= 0:
        break
    else:
        print(s)

