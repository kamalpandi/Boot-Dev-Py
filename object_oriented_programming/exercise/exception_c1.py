# Assignment
# Take a look at the get_player_record function. It raises an exception for negative player_id's.

# Complete the handle_get_player_record() function.
# It should return the result of get_player_record but if an IndexError is raised it will instead return the string: index is too high.
# Otherwise,
# if any other exception is raised, handle it and return its inner message.


def handle_get_player_record(players_id):
    try:
        result = get_player_record(players_id)
        return result
    except IndexError:
        return "index is too high"
    except Exception as e:
        return e


# Don't edit below this line


def get_player_record(player_id):
    if player_id < 0:
        raise Exception("negative ids not allowed")
    players = [
        {"name": "Slayer", "level": 128},
        {"name": "Dorgoth", "level": 300},
        {"name": "Saruman", "level": 4000},
    ]
    return players[player_id]
