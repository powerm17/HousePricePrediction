def real_estate_price_calculator():
    print("Welcome to my real estate average price calculator!")
    
    # Ask user neighborhood name
    neighborhood = input("Enter the neighborhood name: ")
    
    # The number of houses in the neighborhoods is unknown 
    prices = []
    while True:
        add_house_price = input("Would you like to add the price of one more house? (y/n): ")
        if add_house_price.lower() == 'y':
            price = float(input("Enter house price: "))
            prices.append(price)
        elif add_house_price.lower() == 'n':
            break
        else:
            print("Please enter 'y' or 'n'.")
    
    if prices:
        # Calc Average
        avg_price = sum(prices) / len(prices)
        print(f"\nThe average house price in the {neighborhood} neighborhood is {avg_price:.2f}")
    else:
        print(f"\nNo prices entered for the {neighborhood} neighborhood.")
    
    print("Thanks for using the App!")

real_estate_price_calculator()
