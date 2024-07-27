# MEDITATE
# In Fantasy Quest, player characters have spells and abilities that cost mana to cast. Characters can meditate to regenerate mana by converting energy directly into mana. Energy potions can be used to instantly regain energy.

# CHALLENGE
# Complete the meditate function using a while loop. It takes mana, max_mana, energy and energy_potions integers.

# While meditating, a character converts 1 energy into 3 mana for each iteration of the loop.
# mana cannot exceed the max_mana.
# If they have any energy_potions when they run out of energy, they will use 1 energy potion to gain 50 energy and continue meditating.

# A character will stop meditating if either:
# Their mana reaches the max_mana, or
# They run out of energy and energy_potions.
# Return the mana and remaining energy and energy_potions when the character stops meditating.


def meditate(mana, max_mana, energy, energy_potions):
    mana_needed = max_mana - mana
    print("mana needed: ", mana_needed)

    if mana == max_mana:
        print("----")
        return mana, energy, energy_potions

    while mana < max_mana:
        mana_from_energy = energy * 3  # used all energy
        energy = 0

        mana = mana_from_energy + mana
        if mana == max_mana:
            return mana, energy, energy_potions
        elif mana > max_mana:
            print("exceeds max mana")
        return mana, energy, energy_potions
