# Get height of diamond from user
num_rows = int(input("Enter the number of rows: "))


def diamond_shape(height):
    """
    Creates a diamond shape using asterisks and spaces
    Args:
        height: Integer representing number of rows in top half of diamond
    """
    # Print top half (pyramid)
    for i in range(height):
        spaces = " " * (height - i - 1)
        stars = "* " * (i + 1)
        print(spaces + stars)

    # Print bottom half (inverted pyramid excluding middle row)
    for i in range(height-2, -1, -1):
        spaces = " " * (height - i - 1)
        stars = "* " * (i + 1)
        print(spaces + stars)


diamond_shape(num_rows)


# Output:
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
