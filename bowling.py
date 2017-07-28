def score(game):
    result = 0
    frame_index = 1
    in_first_half = True
    for frame in range(len(game)):
        if game[frame] == '/':
            result += 10 - last_roll
        else:
            result += get_value(game[frame])
        if frame_index < 10 and get_value(game[frame]) == 10:
            if game[frame] == '/':
                result += get_value(game[frame+1])
            elif game[frame] in 'Xx':
                result += get_value(game[frame+1])
                if game[frame+2] == '/':
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
        if game[frame] in 'Xx':
            in_first_half = True
            frame_index += 1
    return result


def get_value(char):
    if char in '123456789':
        return int(char)
    elif char in 'Xx/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
