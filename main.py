# calculator
from picture import logo

print(logo)
# add
def add(n1, n2):
    return n1 + n2


# subtract
def subtract(n1, n2):
    return n1 - n2


# divison
def division(n1, n2):
    return n1 / n2


# multiply
def multiply(n1, n2):
    return n1 * n2


# dic empty
calculator = {
    "+": add,
    "-": subtract,
    "/": division,
    "*": multiply
}

# input

dabro = True

while dabro:
    # input
    n1 = float(input("Choose the first number: "))

    for icons in calculator:
        print(icons)
    choosed = input("choose operation: ")

    n2 = float(input("choose the second number: "))

    calcf_function = calculator[choosed]

    answer = int(calcf_function(n1, n2))

    print(f"{n1} {choosed} {n2} = {answer}")

    #saved answer
    saved_answer = answer

    asker = input(f"last answer {answer}. Do you want to continue? press 'y' or 'n' to end. : ").lower()

    if asker == "y":
        print(f"Previouse answer '{saved_answer}' and operator '{choosed}' ")
        continue

    elif asker == "n":
        dabro = False
    else:
        wrong_character = True

        while wrong_character:
            asker = input("invalid symbol 'y' To continue 'n' to disable try again: ").lower()
            if asker == "y":
                print(f"Previouse answer {saved_answer} and operator {choosed}")
                wrong_character = False
            elif asker == "n":
                wrong_character = False
                dabro = False
            else:
                wrong_character = True

# finish

print("Thank you for useing my calculator")