# x = -10        # int whole numbers
# y = -3.14     # float or decimals
# z = 1 + 2j   # complex special numbers mostly for formulars


# print(x)
# print(y)
# print(z)


def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# INSTRUCTIONS FOR TESTING
# 1. Launch your terminal and run the code
# 2. Run the code -> python 3_variables_numbers.py