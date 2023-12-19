import os

os.system('cls')

def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1/n2
operations = {
'/': div,
'+': add,
'-': sub,
'*': mul
}
n1 = float(input("What's the first number?: "))

is_done = False
while is_done == False:
    operation = input("+\n-\n*\n/\nPick an operation: ")
    n2 = float(input("What's the next number?: "))
    symbol = operations[operation]
    answer = float(symbol(n1, n2))
    print(str(n1), operation, str(n2) + " = " + str(answer))
    continu = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
    if continu == 'n':
        is_done = True
    else:
        n1 = answer


