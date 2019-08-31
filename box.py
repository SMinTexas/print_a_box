# Given a height and width, input by the user, print a box consisting of * 
# characters as its border.

square_width = int(input("Width? "))
square_height = int(input("Height? "))

print('*' * square_width)

for number in range(square_height - 2):
    print('*' + ' ' * (square_width - 2) + '*')

print('*' * square_width)