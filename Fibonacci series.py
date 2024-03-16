def fibonacci(n):
  """
  This function generates the Fibonacci sequence up to a specified term n.

  Args:
      n: An integer representing the number of terms in the Fibonacci sequence.

  Returns:
      A list containing the first n terms of the Fibonacci sequence.
  """
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

# Get user input
n = int(input("Enter the number of terms in the Fibonacci sequence: "))

# Generate the Fibonacci sequence
fibonacci_sequence = [fibonacci(i) for i in range(n)]

# Print the Fibonacci sequence
print(fibonacci_sequence)
