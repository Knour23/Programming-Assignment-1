# cycle.py

# Function to generate the next number in the sequence
def next_value(x, a, b, M):
    return (a * x + b) % M

# Function to compute the cycle length using Floyd's algorithm
def floyd_cycle_length(a, b, c, M):
    # Phase I: Tortoise and Hare - Finding the point where they meet
    tortoise = next_value(c, a, b, M)  # x1
    hare = next_value(next_value(c, a, b, M), a, b, M)  # x2
    
    # Continue moving the tortoise by 1 step and hare by 2 steps until they meet
    while tortoise != hare:
        tortoise = next_value(tortoise, a, b, M)
        hare = next_value(next_value(hare, a, b, M), a, b, M)
    
    # Phase II: Find the starting point of the cycle
    # Reset tortoise to the beginning
    tortoise = c
    while tortoise != hare:
        tortoise = next_value(tortoise, a, b, M)
        hare = next_value(hare, a, b, M)
    
    # Phase III: Compute the cycle length
    # Once the tortoise and hare meet, we can compute the length of the cycle
    cycle_length = 1
    hare = next_value(tortoise, a, b, M)
    while tortoise != hare:
        hare = next_value(hare, a, b, M)
        cycle_length += 1
    
    return cycle_length

# Main function for user input and cycle length calculation
if __name__ == "__main__":
    # Taking inputs for a, b, c, and M
    a, b, c, M = map(int, input("Enter values for a, b, c, M: ").split())
    
    # Compute the cycle length
    cycle_len = floyd_cycle_length(a, b, c, M)
    
    # Output the cycle length
    print(f"Cycle length is {cycle_len}.")
