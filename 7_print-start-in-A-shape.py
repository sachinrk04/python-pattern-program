
def print_A_shape(height):
    for row in range(height):
        # Calculate spaces needed before the pattern
        spaces = " " * (height - row - 1)

        if row == 0:
            # Top point of A
            print(spaces + "* ")
        elif row == height // 2:
            # Middle horizontal line
            print(spaces + "* " * (row + 1))
        else:
            # Two sides of A
            inner_spaces = " " * (2 * row - 1)
            print(spaces + "*" + inner_spaces + "*")


print_A_shape(7)

# Output:
#      *
#     * *
#    *   *
#   * * * *
#  *       *
# *         *
