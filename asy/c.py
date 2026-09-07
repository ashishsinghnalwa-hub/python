def quadratic_time(number):
    iterations = 0
    for outer_index in range(number):
        for inner_index in range(number):
            iterations += 1
        print()
    print("When n is:", number, "iterations:", iterations, "\n")

quadratic_time(10)
quadratic_time(20)
quadratic_time(30)
print('\nThe number of iterations grows as n^2: O(n^2).')