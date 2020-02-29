

# O(n)
def n_demo(n):
  print(n)
  # base case
  if n == 0:
    return
  # recursive case
  n_demo(n - 1)

# O(2 ^ n)
# each call to two_n_demo spawns two more calls. This explodes exponentially
def two_n_demo(n):
  print(n)
  if n == 0:
    return
  two_n_demo(n - 1)
  two_n_demo(n - 1)
  

# O(log n)
# dividing the input will cause this to finish very quickly
def divide_n_demo(n):
  print(n)
  if n <= 1:
    return
  
  divide_n_demo(n / 2)