#ultimo ejercicio del dia


def funcion(a, b, *args, **kwargs):
    print("a=", a)
    print("b=", b)
    for arg in args:
        print("arg=", arg)
    for key, value in kwargs.items():
     print("key=", key, "=", value)

funcion(1,2,14,21,24,36, x="luis", y="sol de mexico", c="mexico")
