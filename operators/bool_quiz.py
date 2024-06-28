# What is the value of 'result'?

# TrueFalse


is_tall = True
is_fat = True
is_skinny = False
is_short = False
result = (is_tall and is_fat) or (is_skinny and is_short)
print(result)


# SHOULD SERVE DRINKS
# ASSIGNMENT
# In Fantasy Quest, players can go to a town's local pub. Drinking virtual beer refills their stamina!

# Complete the function that determines if a bartender should serve drinks to a customer. Only return True if all of these conditions apply:

# The customer's age is 21 or older
# The bartender is working
# The time is at least 5 but no later than 10
# TIP - IF STATEMENTS DON'T NEED A COMPARISON
# Where "is_big" is a boolean value, the following statements are identical:

# if is_big:
#     # ...
# Copy icon
# if is_big == True:
#     # ...
# Copy icon
# The first option should be preferred due to length; however, the second is more readable. The == True is redundant.


# solution

def should_serve_customer(customer_age, on_break, time):
    if (customer_age>=21 and (not on_break))and (time>=5 and time<=10):
        return True
    return False
    pass
