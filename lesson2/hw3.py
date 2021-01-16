print("Hello! You can calculate smth here, but be attentive ^-^")
print("What would u like to calculate?")
print("At first, enter one number, that enter one operator and one more number and one more operator.../n")

oper = None
res = 0

while oper != "=":
    try:
        num = float(input("Please, enter a number: "))
    except ValueError:
        print("I am a joke to you???)))")
        continue
    if oper is None:
        res = num
    elif oper == "+":
        res += num
    elif oper == "-":
        res -= num
    elif oper == "*":
        res *= num
    elif oper == "/":
        try:
            res /= num
        except ZeroDivisionError:
            print("Okey, I know, miracles happen, but not zero division. So, try again ")

    while oper in ("+" or "-" or "/" or "+" or "="):
        oper = input()
        oper1 = oper.split(' ')
        if len(oper1) == 1:
            oper = oper
        else:
            continue
        if oper not in ("+" or "-" or "/" or "+" or "="):
            print("What do u mean? I accepted +, -, * or /")
            continue
        elif "=":
            continue
    print(f"result = {res}")
