# C to F
# Function takes in value, does conversion and puts answer into a list


def to_c(from_f):
    centigrade1 = (from_f - 32)
    centigrade = centigrade1 * 5/9
    return centigrade


# main routine
temperatures = [32, 104, 212]
converted = []

for item in temperatures:
    answer = to_c(item)
    ans_statement = "{} degrees F is {} degrees c".format(item, answer)
    converted.append(ans_statement)

print(converted)
