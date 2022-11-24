from averager_decorator import make_averager, make_averager_2, Averager


if __name__ == "__main__":
    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))
    print("-------------------")
    avg2 = Averager()
    print(avg2(10))
    print(avg2(11))
    print(avg2(12))
    print("------- INSPECTING FUNC ------------")
    print(
        f"free variables: {avg.__code__.co_freevars} \n"
        f"closure: {avg.__closure__} \n"
        f"cell contents: {avg.__closure__[0].cell_contents} \n"
        f"co_varnames: {avg.__code__.co_varnames} \n"
    )