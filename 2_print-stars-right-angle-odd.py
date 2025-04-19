# 2. Print stars in right angle triangle with odd number of stars
num_rows = int(input("Enter the number of rows: "))


def odd_right_angle_triangle(height):
    result = ""
    for i in range(height):
        result += '*' * (i * 2 + 1) + '\n'
    return result


result = odd_right_angle_triangle(num_rows)

# Test the function
print(result)

# Output:
# *
# ***
# *****
