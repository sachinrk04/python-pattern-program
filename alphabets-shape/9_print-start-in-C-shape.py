def print_C_shape(height):
    for row in range(height):
        if row == 0 or row == height-1:
            print(' *'*(height-3))
        elif row == 1 or row == height-2:
            print('* '+' '*(height-1) + '*')
        else:
            print('* '+' '*(height-2))


print_C_shape(7)

# Output:
#  * * * *
# *       *
# *
# *
# *
# *       *
#  * * * *
