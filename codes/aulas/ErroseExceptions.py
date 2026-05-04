while True:
    try:
        num = float(input('algo:   '))
        dob = num * 2

    except:
        print('not a number')
    else:
        print(dob)
        break
    finally:
        print('fim') 