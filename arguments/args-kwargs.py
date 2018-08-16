## arguments and kwargs

def argument_functions(*args,**kwargs):

    if args and kwargs and len(args) == len(kwargs):
        args = iter(args)
        print({value: next(args) for value in kwargs.values()})

    elif not kwargs:
        print("Countries: {}".format(args))
    elif not args:
        for country, capital in kwargs.items():
            print("Country: {} and its Capital: {}".format(country.upper(), capital))
    else:
        print("Just print arguments: {} and keyword-arguments: {}".format(args, kwargs))




if __name__ == "__main__":


    ## print countries
    argument_functions("USA", "Canada", "UK")
    print("*************------****************")


    # print country and its capital
    argument_functions(
        india= "Delhi", japan="tokyo",
        )

    print("*************------****************")

    # print winner and loser :)
    argument_functions(
        "Winner", "loser",
        india= "Delhi", japan="tokyo"
    )

    print("*************------****************")
    # print arguments and keywords passed

    argument_functions(
        "Winner", "loser",
        india="Delhi", japan="tokyo", france="paris"
    )

#Output:
    # Countries: ('USA', 'Canada', 'UK')
    # *************------****************
    # Country: INDIA and its Capital: Delhi
    # Country: JAPAN and its Capital: tokyo
    # *************------****************
    # {'tokyo': 'loser', 'Delhi': 'Winner'}
    # *************------****************
    # Just print arguments: ('Winner', 'loser') and keyword-arguments: {'india': 'Delhi', 'france': 'paris', 'japan': 'tokyo'}
