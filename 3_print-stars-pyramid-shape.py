# Get the number of rows from user input
num_rows = int(input("Enter the number of rows: "))


def pyramid_shape(height):
    """
    Creates a pyramid shape using asterisks and spaces
    Args:
        height: Integer representing number of rows in pyramid
    Returns:
        String containing the pyramid pattern
    """
    result = ""
    for i in range(height):
        # Calculate leading spaces - decreases as we go down
        spaces = " " * (height - i - 1)
        # Calculate stars with spaces between them - increases as we go down
        stars = "* " * (i + 1)
        # Combine spaces and stars for this row and add newline
        result += spaces + stars + "\n"
    return result


# Print the pyramid pattern
# end="" prevents extra newline at the end
print(pyramid_shape(num_rows), end="")

# Output:
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
