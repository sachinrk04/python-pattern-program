# Get the number of rows from user input
num_rows = int(input("Enter the number of rows: "))


def reverse_pyramid_shape(height):
    """
    Creates a reverse pyramid shape using asterisks and spaces
    Args:
        height: Integer representing number of rows in pyramid
    Returns:
        None - prints pattern directly
    """
    # Iterate from height down to 1 (inclusive)
    for i in range(height, 0, -1):
        # Calculate leading spaces - increases as we go down
        spaces = " " * (height - i)
        # Calculate stars with spaces between them - decreases as we go down
        stars = "* " * i
        # Print spaces and stars for this row
        print(spaces + stars)


# Print the reverse pyramid pattern
reverse_pyramid_shape(num_rows)


# Output:
#   * * * * *
#    * * * *
#     * * *
#      * *
#       *
