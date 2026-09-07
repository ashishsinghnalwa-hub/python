def linear_time(number):
    iterations = 0
    for index in range(number):
        iterations += 1
    print("When n is:", number, "iterations:", iterations)

linear_time(5)
linear_time(10)
linear_time(100)
print('\nThe number of iterations grows linearly with n: O(n).')