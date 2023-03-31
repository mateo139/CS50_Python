def f (*args, **kwargs):    #*args -> some number of arguments,  **kwargs-> some number of key word arguments
    print("Positional:", kwargs)


f(dollars = 10, zlotys = 50, euros= 100)