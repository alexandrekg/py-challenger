def timeConversion(s):
    if 'PM' in s:
        removing_timechar = s.replace('PM', '')
    else:
        removing_timechar = s.replace('AM', '')

    split_time = removing_timechar.split(':')

    if 'PM' in s:
        if split_time[0] < '12':
            add_time = [str(int(split_time[0]) + 12)]
        else:
            add_time = [split_time[0]]
    elif split_time[0] == '12' and split_time[1] > '0':
        add_time = ['0' + str(int(split_time[0]) - 12)]
    else:
        add_time = [split_time[0]]

    result = ":".join(add_time + split_time[1:])
    print(result)
    return result


if __name__ == '__main__':
    s = '12:45:54PM'
    result = timeConversion(s)
