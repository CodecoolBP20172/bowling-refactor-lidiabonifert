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
            elif game[frame] == 'X' or game[frame] == 'x':
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
        if game[frame] == 'X' or game[frame] == 'x':
            in_first_half = True
            frame_index += 1
    return result


def get_value(char):
    if char == '1' or char == '2' or char == '3' or \
       char == '4' or char == '5' or char == '6' or \
       char == '7' or char == '8' or char == '9':
        return int(char)
    elif char == 'X' or char == 'x' or char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
