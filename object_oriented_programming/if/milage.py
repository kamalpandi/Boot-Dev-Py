def has_enough_gas(gallons_in_car, miles_one_way, miles_per_gallon):
    milage = gallons_in_car * miles_per_gallon
    if milage >= miles_one_way*2:
        gallons_needed = (miles_one_way*2)-(gallons_in_car * miles_per_gallon)
        print(gallons_needed)
        return True
    else:
        gallons_needed = (miles_one_way*2)-(gallons_in_car * miles_per_gallon)
        print(gallons_needed)
        return False
    # gallons_needed 
    pass
