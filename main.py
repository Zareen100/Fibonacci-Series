# Function to print Fibonacci series up to n terms
def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Get the number of terms from the user
try:
    n = int(input("Enter the number of terms: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        print("Fibonacci Series up to", n, "terms:")
        print(fibonacci(n))
except ValueError:
    print("Invalid input! Please enter an integer.")
