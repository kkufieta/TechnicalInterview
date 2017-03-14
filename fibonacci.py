def get_fib_loop(position):
  if position == 0:
    return 0
  if position == 1:
    return 1
  first = 0
  second = 1
  next_num = first + second

  for i in range(2, position):
    first = second
    second = next_num
    next_num = first + second

  return next_num

def get_fib_recursively(position):
  if position == 0 or position == 1:
    return position

  return get_fib_recursively(position - 2) + get_fib_recursively(position - 1)
