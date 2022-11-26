hours = range(9, 24, 2)
minutes = range(0, 60, 15)

for hour in hours:
    for minute in minutes:
        print(f'Alarm time {hour}:{minute}')
        