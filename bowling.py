def score(game):  # Count score for a bowling game.
    result = 0
    frame_index = 1
    in_first_half = True
    try:
        for frame in range(len(game)):
            if is_spare(game[frame]):
                result += 10 - last_roll
            else:
                result += get_value(game[frame])
            result = check_if_last_round(frame_index, game, frame, result)
            last_roll = get_value(game[frame])
            if not in_first_half:
                frame_index += 1
            if in_first_half:
                in_first_half = False
            else:
                in_first_half = True
            if is_strike(game[frame]):
                in_first_half = True
                frame_index += 1
        return result
    except ValueError:
        print('Wrong input! Please type in: numbers 1-9 for score, "X" for strike or "/" for spare!')


def check_if_last_round(frame_index, game, frame, result):
    if frame_index < 10 and get_value(game[frame]) == 10:
        if is_spare(game[frame]):
            result += get_value(game[frame+1])
        elif is_strike(game[frame]):
            result += get_value(game[frame+1])

            if is_spare(game[frame+2]):
                result += 10 - get_value(game[frame+1])
            else:
                result += get_value(game[frame+2])
    return result

def is_strike(frame):  # Checks for strike marker.
    return frame in 'Xx'


def is_spare(frame):  # Checks for spare marker.
    return frame == '/'


def get_value(char):  # Matches the input to the score and return it or raise an error in case it cannot.
    if char in '123456789':
        return int(char)
    elif is_strike(char) or is_spare(char):
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError
