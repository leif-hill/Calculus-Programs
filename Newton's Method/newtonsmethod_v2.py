import math

def root(num, initial_guess):
    approximated = False
    iteration = 0

# checks for and prevents divide by zero error
    if (initial_guess**2 - num == 0):
            initial_guess += 1
            print("Error: Results in zero, adding one to initial iteration.")

    x = initial_guess

#loops until sqrt is found
    while not approximated:
        percent_diff = (abs(x - math.sqrt(num)) / ((math.sqrt(num)+x)/2) * 100.0)
    #checks if iteration value matches real sqrt
        if math.isclose(x, math.sqrt(num), rel_tol=1e-10): 
            approximated = True
            print("Finished.")

        else:
            x = x - ((x**2 - num)/(2*x)) #Newton's Method
            iteration += 1

            # percent_diff = (abs(x - math.sqrt(num)) / ((math.sqrt(num)+x)/2) * 100.0) #Finds percent difference between iteration and actual root

            print("*********************")
            print("Iteration #{}".format(iteration), x)
            print("Absolute Error:{}".format((math.sqrt(num)-x)), "Approx. ({}%)".format(round(percent_diff, 3)))

root(23, 24)

