num_rows = int(input("Enter the number of rows: "))


def invert_right_angle(height):
    for i in range(height, 0, -1):
        print('*' * i)


invert_right_angle(num_rows)

# Output:
# *****
# ****
# ***
# **
# *
