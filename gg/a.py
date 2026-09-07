travel_to = "Agra"
ticket_price = 201.60
passenger_name = "John Doe"
no_of_tickets = 3
cost_of_one_ticket = ticket_price * no_of_tickets   # this * will multiply
travel_availability = False
voucher_code = "AgRaejxvdlsbc5246"
used_code = 30
print(f"Passenger Name: {passenger_name}")  #we use {} here to format the string and include the value of passenger_name in the output  
print(f"Destination: {travel_to}")
print(f"Ticket Price: ${ticket_price:.2f}")   #2f is used to format the float value to 2 decimal places
print(f"Number of Tickets: {no_of_tickets}")
print(f"Total Cost: ${cost_of_one_ticket:.2f}")
print(f"Voucher Code: {voucher_code}")
print(f"Used Code: {used_code}")
print(f"Availability: {travel_availability}")
print(type(travel_to))  #this will print the data type of travel_to variable
print(type(ticket_price))  
print(type(no_of_tickets))  
print(type(cost_of_one_ticket))  
print(type(travel_availability))  
print(type(voucher_code))
print(type(used_code))  
using_voucher_code = ticket_price - used_code
print(f"Cost with Voucher: ${using_voucher_code:.2f}")
print(f"is the cost of one ticket greater than the used code? {cost_of_one_ticket > used_code}")  #this will print True or False based on the comparison
print(f"is the cost of one ticket less than the used code? {cost_of_one_ticket < used_code}")  
print(f"is the cost of one ticket equal to the used code? {cost_of_one_ticket == used_code}")  
print(f"is the destination available for travel? {travel_availability}")
print("swapping the values of cost_of_food and cost_of_one_ticket")
cost_of_food = 500
print("====BEFORE SWAPPING====")
print(f"cost_of_food: ${cost_of_food}")
print(f"cost_of_one_ticket: ${cost_of_one_ticket}")
cost_of_food, cost_of_one_ticket = cost_of_one_ticket, cost_of_food # like this @,3 = 3,@ symmetrically
print("---AFTER SWAPPING---")
print(f"cost_of_food: ${cost_of_food}")
print(f"cost_of_one_ticket: ${cost_of_one_ticket}")
print("====FINAL STATUS====")
print(f"Passenger Name: {passenger_name}")
print(f"Destination: {travel_to}")
print(f"Ticket Price: ${ticket_price:.2f}")
print(f"Number of Tickets: {no_of_tickets}")
print(f"Total Cost: ${cost_of_one_ticket:.2f}")