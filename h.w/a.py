print("====== WELCOME TO MY TRAIN SEAT FINDER ======")
seats = [142,156, 178, 189, 200, 210, 220, 230, 240, 250]
your_seat = 230
print("available seats are: ", seats)
print("your seat is: ", your_seat)
def binary_search(seats, your_seat):
    low = 0
    high = len(seats) - 1
    steps = 0
    while low <= high:
        mid = (low + high) // 2
        steps += 1
        if seats[mid] == your_seat:
            return steps, mid
        elif seats[mid] < your_seat:
            low = mid + 1
        else:
            high = mid - 1
    return steps, -1
steps,index = binary_search(seats, your_seat)
if index != -1:
    print("Your seat is found at index: ", index)
    print("Total steps taken to find your seat: ", steps)
