def onssquretime(n):
    iterations = 0
    for i in range(n):
        for e in range(n):
            iterations +=1
        print("")
    print("when n is: ", n, "iterations: ", iterations, "\n")
onssquretime(10)
onssquretime(20)
onssquretime(30)
print("\n write every "n" the time taken equals n^2")
print("o(n^2) time complexity")