# C to F
# Function takes in value, does conversion and puts answer into a list


def to_c(from_f):
    Centigrade = (from_f * 9/5 + 32)
    return Centigrade


# main routine
temperatures = [0, 40, 100]
converted = []

for item in temperatures:
    answer = to_c(item)
    ans_statement = "{} degrees C is {} degrees F".format(item, answer)
    converted.append(ans_statement)

print(converted)
