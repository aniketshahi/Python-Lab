def generate_fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

# Get user input for the number of terms in the Fibonacci series
try:
    n_terms = int(input("Enter the number of Fibonacci terms to generate: "))
    if n_terms <= 0:
        raise ValueError("Number of terms should be a positive integer.")
except ValueError as e:
    print(f"Error: {e}")
    exit(1)

# Generate and display the Fibonacci series
fibonacci_series = generate_fibonacci(n_terms)
print(f"Fibonacci Series with {n_terms} terms: {fibonacci_series}")
