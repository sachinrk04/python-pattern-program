def print_F_shape(height):
    for row in range(height):
        if row == 0:
            print('* '*(height-2))
        elif row == height//2:
            print('* '*(height-3))
        else:
            print('* '+' '*(height-2))


print_F_shape(7)

# Output:
# * * * * *
# *
# * * * *
# *
# *
