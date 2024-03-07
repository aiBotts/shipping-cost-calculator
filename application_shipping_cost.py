# Describing to the user what this program does
print()
print('-----This program calculates the total shipment per cost of goods-----')
print()

# Creating a variable for the answer 'y'
keep_going = 'y'


# Calculate the total cost after shipping by using a while loop
while keep_going == 'y':

    # Asking the user to enter how much they spent on goods
    total_cost = float(input("What is the total cost before shipping? "))

    # Creating each variable for the cost of shipping
    lowest_cost = total_cost <= 30.00
    mid1_cost = total_cost >= 30.1 and total_cost <= 49.99
    mid2_cost = total_cost >= 50.00 and total_cost <= 74.99
    highest_cost = total_cost >= 75.00

    # Display the error message for total cost amount under 0.00
    if total_cost < 0.00:
        print('Please enter a number above 0')
        print()
        continue                                  # Using the continue statement to go back to the beginning of loop

    # Running the loop for the shipping cost after total cost is put in
    if lowest_cost:
        print()
        print('Your shipping is: $ 5.95')
        print('That brings your total cost to: $', total_cost + 5.95)
        print()
        keep_going = input('Do you have another package to ship? (Enter y for yes): ')
        print()
        continue
    elif mid1_cost:
        print()
        print('Your shipping is: $ 7.95')
        print('That brings your total cost to: $', total_cost + 7.95)
        print()
        keep_going = input('Do you have another package to ship? (Enter y for yes): ')
        print()
        continue
    elif mid2_cost:
        print()
        print('Your shipping is: $ 9.95')
        print('That brings your total cost to: $', total_cost + 9.95)
        print()
        keep_going = input('Do you have another package to ship? (Enter y for yes): ')
        print()
        continue
    elif highest_cost:
        print()
        print('Your shipping is: Free!')
        print('That brings your total cost to: $', total_cost)
        print()
        keep_going = input('Do you have another package to ship? (Enter y for yes): ')
        print()
        continue

