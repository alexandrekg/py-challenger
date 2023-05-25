def timeConversion(s):
    if 'PM' in s:
        removing_timechar = s.replace('PM', '')
    else:
        removing_timechar = s.replace('AM', '')

    split_time = removing_timechar.split(':')
    add_time = [str(int(split_time[0]) + 12 if 'PM' in s else - 12)]
    return ":".join(add_time + split_time[1:])


if __name__ == '__main__':
    s = '07:05:45PM'
    result = timeConversion(s)
