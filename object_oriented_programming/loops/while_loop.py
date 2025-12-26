# WHILE
# Python has another type of loop, the while loop. It's a loop that continues while a condition remains True. The syntax is simple:

# while 1:
#     print("1 evaluates to True")

# # prints:
# # 1 evaluates to True
# # 1 evaluates to True
# # (...continuing)
# Copy icon
# The example above is hardcoded to continue forever, creating an infinite loop. Typically, a while loop condition is a comparison or variable, and it determines when the loop ends:

# num = 0
# while num < 3:
#     num += 1
#     print(num)

# # prints:
# # 1
# # 2
# # 3
# # (the loop stops when num >= 3)
# Copy icon
# ASSIGNMENT
# In Fantasy Quest, player characters regenerate health when standing still while away from enemies. This means they will gain health but can't run from enemies that are coming towards them while regenerating.

# Complete the regenerate function using a while loop. It takes current_health, max_health and enemy_distance integers.

# While regenerating health, a character gains health until it reaches the max_health amount.
# For every 1 health a character gains, the enemy_distance shortens by 2.
# If an enemy is a distance of 3 or less from the character, the character stops gaining health.
# Return the new current_health after health regeneration stops.\


def regenerate(current_health, max_health, enemy_distance):


    while enemy_distance>=3:
        current_health = current_health+1
        enemy_distance = enemy_distance-2
        if current_health == max_health:
            return current_health
    return current_health
    

