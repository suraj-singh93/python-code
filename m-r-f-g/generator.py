def fibonaci(high):
    a,b = 0 ,1
    for i in range(high):
        yield a
        b,a = a+b,b





for i in fibonaci(15):
    print(i)
