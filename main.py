"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
###

def simple_work_calc(n, a, b):
  """Compute the value of the recurrence $W(n) = aW(n/b) + n
  
  Params:
  n......input integer
  a......branching factor of recursion tree
  b......input split factor
  
  Returns: the value of W(n).
  Base case W(1) = 1
  Base case 2 W(0) = 0
  """
  
  if n==1:
    return 1
    
  if n == 0: 
    return 0

  return a*simple_work_calc(n//b, a, b) + n
    

def test_simple_work():
  """ done. """
  assert simple_work_calc(10, 2, 2) == 36
  assert simple_work_calc(20, 3, 2) == 230
  assert simple_work_calc(30, 4, 2) == 650
  assert simple_work_calc(20, 2, 2) == 92
  assert simple_work_calc(30, 2, 2) == 128
  assert simple_work_calc(40, 2, 2) == 224

def work_calc(n, a, b, f):
  """Compute the value of the recurrence $W(n) = aW(n/b) + f(n)
  
  Params:
  n......input integer
  a......branching factor of recursion tree
  b......input split factor
  f......a function that takes an integer and returns 
  the work done at each node 
  
  Returns: the value of W(n).
  """
  # print("runtime")
  if n == 1:
    return 1
  if n == 0:
    return 0
  return a*work_calc(n//b, a, b, f) + f(n)

def test_work():
  """ done. """
  assert work_calc(10, 2, 2,lambda n: 1) == 15
  assert work_calc(10, 2, 2,lambda n: n*n) == 174
  assert work_calc(10, 2, 2,lambda n: n) == 36
  assert work_calc(20, 1, 2, lambda n: n*n) == 530
  assert work_calc(30, 3, 2, lambda n: n) == 300
  assert work_calc(20, 2, 2,lambda n: 1) == 31
  assert work_calc(30, 2, 2, lambda n: n*n) == 1634
  assert work_calc(40, 2, 2, lambda n: n) == 224

def span_calc(n, a, b, f):
  """Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)
  
  Params:
  n......input integer
  a......branching factor of recursion tree
  b......input split factor
  f......a function that takes an integer and returns 
         the work done at each node 
  
  Returns: the value of W(n).
  """
  # TODO

  if n == 1:
    return 1
  if n == 0:
    return 0
  return span_calc(n//b, a, b, f) + f(n)


def q5_work_a(n):
    return n**3

def q5_work_b(n):
    return n**1

def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
  """
  Compare the values of different recurrences for 
  given input sizes.
  
  Returns:
  A list of tuples of the form
  (n, work_fn1(n), work_fn2(n), ...)
  
  """
  
  
  
  result = []
  for n in sizes:
    # compute W(n) using current a, b, f
    result.append((
      n,
      work_calc(n, 2, 2, work_fn1),
      work_calc(n, 2, 2, work_fn2)
      ))
  return result



def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_work():
  # curry work_calc to create multiple work
  # functions taht can be passed to compare_work
  
  # create work_fn1
  # create work_fn2

  def work_fn1(n):
    return n**2
    
  def work_fn2(n):
    return n**3


  
    

  results = compare_work(work_fn1, work_fn2)
  print_results(results)


def test_compare_span():
  """
  Implement `test_compare_span` to create a new comparison function for comparing span functions. 
  Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. 
  Confirm that everything matches up as it should. 
  """
  
  def span_fn1(n):
    return n**2
    
  def span_fn2(n):
    return n

  fn1_span = span_calc(10, 2, 2, span_fn1)
  fn2_span = span_calc(10, 2, 2, span_fn2)
  print("fn1_span: %d \n" % fn1_span)
  print("fn2_span: %d \n" % fn2_span)



if __name__ == "__main__":
  test_simple_work()
  test_work()
  
  # print("Work ^")
  test_compare_span()
  # print("Span ^")
  #print("Question 5:\n")
  #test_compare_work()
  
  