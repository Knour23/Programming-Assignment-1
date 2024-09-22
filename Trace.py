# Function to generate M values of x and append them to a list x_list
def print_iterates(a, b, c, M):
    x = c
    x_list = []
    x_list.append(x)

    # Generate M iterates and append them to the list
    for i in range(1, M):
        x = (a * x + b) % M
        x_list.append(x)

    # Call to print the iterates nicely
    print_iterates_nicely(x_list)

    # Call to the Floyd cycle detection function
    Floyd(x_list)

# Function to print the elements nicely with 16 elements per line, and 4 spaces per iterate
def print_iterates_nicely(x_list):
    i = 0
    for j in x_list:
        # Each element is printed with 4 spaces
        print(f"{j:>4}", end=" ")
        i += 1
        # Print a new line after every 16 elements
        if i % 16 == 0:
            print()
    print()  # For a new line after the last line of output

# Floyd's cycle detection algorithm to find the cycle length in the x_list
def Floyd(x_list):
    slow, fast = 0, 0
    list_len = len(x_list)

    # Move the slow pointer by 1 and fast pointer by 2
    while True:
        slow = (slow + 1) % list_len
        fast = (fast + 2) % list_len
        if x_list[slow] == x_list[fast]:
            break

    # Cycle detection - now calculate the cycle length
    cycle_element = x_list[slow]
    cycle_length = 1
    fast = (fast + 1) % list_len
    while x_list[fast] != cycle_element:
        fast = (fast + 1) % list_len
        cycle_length += 1

    # Print the cycle length
    print(f"Cycle length is {cycle_length}")

# Main part of the code to take input and call the function
a, b, c, M = map(int, input("Enter values for a, b, c, M: ").split())
print_iterates(a, b, c, M)
