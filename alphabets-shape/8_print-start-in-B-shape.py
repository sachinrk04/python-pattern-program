def print_B_shape(height):
    for row in range(height):
        if row == 0 or row == height//2 or row == height-1:
            # Print horizontal lines
            print('* ' * (height-3))
        else:
            # Print vertical lines with space between
            print('*' + ' ' * ((height-3)*2-1) + '*')


print_B_shape(7)

# Output:
# * * * *
# *       *
# *       *
# * * * *
# *       *
# *       *
# * * * *
