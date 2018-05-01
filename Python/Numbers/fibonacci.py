number = 8

def fibonacci(number):
  if number < 2:
    raise ValueError("Number has to larger than 2.")

  n1, n2 = 1, 1
  sum = 0

  print(n1, n2, end=' ')
  while sum < number:
    sum = n1 + n2
    if sum > number:
      raise ValueError("Does not have Fibonacci sequence match exactly to that number.")

    print(sum, end=' ')
    n1 = n2
    n2 = sum

fibonacci(number)
