num_rows = int(input("Enter the number of rows: "))


def odd_pyramid_shape(height):
    result = ""
    for i in range(height):
        result += ' ' * (height - i - 1) + '*' * (i * 2 + 1) + '\n'
    return result


result = odd_pyramid_shape(num_rows)
print(result)

# Output:
#     *
#    ***
#   *****
#  *******
# *********
