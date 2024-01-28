#For example, If the given int is 7536,
# the output shall be “6 3 5 7“,
# with a space separating the digits.

number = int(input('Please provide a number:'))
reverse = str(number)[::-1]
output = ' '.join(reverse)
print(output)