import math
approximated = False

def root(num, initial_guess, iterations):
    global approximated
    iteration = 0
    if (initial_guess**2 - num == 0):
            initial_guess += 1
            print("Error: Results in zero, adding one to initial iteration.")
    x = initial_guess
    while not approximated:
        x = x - ((x**2 - num)/(2*x))
        iteration += 1
        print("Absolute Error: ", (math.sqrt(num)-x))

        print("Iteration #", iteration, x)
        if iteration >= iterations:
            approximated = True
            print("Finished.")

root(10, 2, 5)