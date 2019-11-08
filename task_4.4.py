# 1-----------------------------------------
a = "I am global variable!"


def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():

        a = "I am local variable!"
        print(a)

    return inner_function


f = enclosing_funcion()
f()
# 2-----------------------------------------
a = "I am global variable!"


def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():

        global a
        print(a)


# 3-----------------------------------------
a = "I am global variable!"


def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():

        nonlocal a
        print(a)
