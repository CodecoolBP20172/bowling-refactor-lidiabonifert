def score(game):
    result = 0
    frame_index = 1
    in_first_half = True
    for frame in range(len(game)):
        if is_spare(game[frame]):
            result += 10 - last_roll
        else:
            result += get_value(game[frame])

        if frame_index < 10 and get_value(game[frame]) == 10:
            if is_spare(game[frame]):
                result += get_value(game[frame+1])
            elif is_strike(game[frame]):
                result += get_value(game[frame+1])

                if is_spare(game[frame+2]):
                    result += 10 - get_value(game[frame+1])
                else:
                    result += get_value(game[frame+2])
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


def is_strike(frame):
    return frame in 'Xx'


def is_spare(frame):
    return frame == '/'


def get_value(char):
    if char in '123456789':
        return int(char)
    elif is_strike(char) or is_spare(char):
        return 10
    elif char == '-':
        return 0
