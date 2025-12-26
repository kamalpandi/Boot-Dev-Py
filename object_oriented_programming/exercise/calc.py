# CHALLENGE
# Complete the calculate_experience_points function.

# The calculate_experience_points function takes a single parameter named level. Determine how many XP are required to get to the specified level from level 1 with 0 XP.

#     #   0xp -> lvl 1 (O * 5)
#     #  +5xp -> lvl 2 (1 * 5)
#     # +10xp -> lvl 3 (2 * 5)
#     # +15xp -> lvl 4 (3 * 5)
#     #------
#     #  30xp

#     calculate_experience_points(4)
#     # returns 30
# TIPS
# The formula:

# (The XP needed for all previous levels) + (1 less than the current level multiplied by 5)

# Remember that we are only calculating the XP needed to reach the level that was passed in.
# That means we need to calculate the XP for all levels up to, but not including, the given level parameter.


def calculate_experience_points(level):
    xp_per_level = 0
    for i in range(0, level):
        xp = i * 5
        xp_per_level = xp + xp_per_level
    return xp_per_level
