import math
import time
import timeit

first = 0
second = 0

# My best attempt using my knowledge of Python

def harmonic_series_loop():
  global first
  start_time = timeit.default_timer()
  calculated = False
  n = 1
  S = 0
  while not calculated:
    if S <= 10:
      S += 1/n
      n += 1
      print(S)
    else:
        calculated = True
        end_time = timeit.default_timer()
        first = (end_time - start_time)
        print("The value of K is {}, found using a While loop.".format(n-1), "This took {}s".format(end_time - start_time))
    

harmonic_series_loop()

#after researching Euler's constant and harmonic series

def harmonic_series_improved(): #satisfies inequality ln(n) + gamma > 10
    global second
    start_time = timeit.default_timer()
    gamma = 0.57721566490153286060651209
    n = math.ceil(math.exp(10 - gamma))
    end_time = timeit.default_timer()
    second = (end_time - start_time)
    print("The value of K is {}, using math that I barely understand.".format(n), "This took {}s".format(end_time - start_time))

harmonic_series_improved()
print("That was {} times faster!".format(round(first/second)))