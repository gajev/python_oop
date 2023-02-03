def print_rhombus(n):
    for row in range(1, n + 1):
        print(" " * (n - row) + "* " * row)
    for row2 in range(n - 1, -1, -1):
        print(" " * (n - row2) + "* " * row2)


number = int(input())
print_rhombus(number)