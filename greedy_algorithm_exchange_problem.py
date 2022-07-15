def exchange_problem(value: int):
    #value = 99
    money = [100,50,25,10,5,1]
    money_to_give = []

    i = 0;

    while value > 0:
        if value >= money[i]:
            money_to_give.append(money[i])
            value -= money[i]
        else:
            i += 1

        print(value)

    print(money_to_give)


exchange_problem(190)

