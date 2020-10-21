# a_list = '1asd23asd45asd6'

# result = [a for a in a_list if a.isdigit()]

# print(result)

def asd(string):
    dave = ''.join([a for a in string if a.isdigit()])

    if dave != []:
        return float(string)
    else:
        return None

print(asd("1.0"))
print(asd("123.0"))
print(asd("234.0234"))