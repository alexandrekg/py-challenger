def timeConversion(s):
    if 'PM' in s:
        removing_timechar = s.replace('PM', '')
    else:
        removing_timechar = s.replace('AM', '')

    split_time = removing_timechar.split(':')

    if 'PM' in s:
        add_time = [str(int(split_time[0]) + 12)]
    else:
        add_time = [str(int(split_time[0]) - 12)]
    result = ":".join(add_time + split_time[1:])
    return result


if __name__ == '__main__':
    s = '07:05:45PM'
    result = timeConversion(s)
