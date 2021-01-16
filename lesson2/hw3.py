print("Hello! You can calculate smth here, but be attentive ^-^")
print("What would u like to calculate?")
print("At first, enter one number, that enter one operator and one more number and one more operator.../n")

op1 = 0
op2 = 0
res = 0

while True:
    try:
        op1 = float(input())
    except ValueError:
        print("I am a joke to you???)))")
    finally:
        op_1 = op1.split(' ')
        if len(op_1) == 1:
            op1 = op1
        else:
            print(f"Oops! You entered too many numbers :( Enter your number again, please.")
            op1 = float(input())

    oper = input()
    oper1 = oper.split(' ')
    if len(oper1) == 1:
        oper = oper
        if "+" or "-" or "/" or "+":
            continue
        elif not "=":
            continue
        elif "=":
            print("n")
            break
        else:
            break
    else:




while True:
    s = input("Знак (+,-,*,/): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print("%.2f" % (x+y))
        elif s == '-':
            print("%.2f" % (x-y))
        elif s == '*':
            print("%.2f" % (x*y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")