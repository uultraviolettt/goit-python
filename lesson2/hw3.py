print("Hello! You can calculate smth here, but be attentive ^-^")
print("What would u like to calculate?")
print("At first, enter one number, that enter one operator and one more number and one more operator.../n")

res = 0
oper = None

while oper != "=":
    try:
        num = float(input("Please, enter a number: "))
    except ValueError:
        print("I am a joke to you???)))")

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
            print("Okay, I know, miracles happen, but not zero division. So, try again ")
            continue

    oper = input("Please, enter an operator: ")
    while oper not in ("+", "-", "/", "+", "="):
        print("What do u mean? I expected +, -, *, / or = ")
        oper = input("Please, enter an operator: ")
        oper1 = oper.split(' ')
        if len(oper1) == 1:
            oper = oper
            continue
    if oper == "=":
        continue
print(f"result = {res}")
