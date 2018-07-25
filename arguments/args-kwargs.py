def argument_functions(*args,**kwargs):
    for arg in args:
        print(arg)
    for key,value in kwargs.items():
        print(key,value)

argument_functions("suraj","test","java",test="phy",date="17/08/2018",duration = 1)
