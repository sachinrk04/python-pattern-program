def print_E_shape(height):
    for row in range(height):
        if row == 0 or row == height-1 or row == height//2:
            print('* '*(height-2))
        else:
            print('* '+' '*(height-2))


print_E_shape(7)

# Output:
# * * * * * *
# *
# * * * * * *
# *
# * * * * * *