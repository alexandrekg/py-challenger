def timeConversion(s):
    removing_pm = s.replace('PM', '')
    split_time = removing_pm.split(':')
    add_time = [str(int(split_time[0]) + 12)]

    print(":".join(add_time + split_time[1:]))


if __name__ == '__main__':
    s = '07:05:45PM'
    result = timeConversion(s)
