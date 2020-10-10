# ctrl alt m - terminate code runner
print("\n") # formatting

def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg
    
    return total


def confusion_engine(*args, operator):
# any number of args but operator
# must! be supplied as a NAMED argument
    if operator == "*":
        return multiply(*args)
        # Have to use * to pass in 4 args
        # instead of one tuple
    elif operator == "+":
        return sum(args)
    else:
        return "You're doing it wrong"

print(confusion_engine(1, 2, 3, 4, operator="*"))

print("\n") # formatting