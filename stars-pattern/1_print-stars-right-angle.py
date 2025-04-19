# 1. Print stars in right angle triangle
num_rows = int(input("Enter the number of rows: "))


def print_right_angle_triangle(height):
    for i in range(height):
        print('*' * (i + 1))


# Test the function
print_right_angle_triangle(num_rows)

# Output:
# *
# **
# ***
# ****
# *****
