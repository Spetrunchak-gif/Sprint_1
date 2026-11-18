times = ('1h 45m,360s,25m,30m 120s,2h 60s')

new_times = times.replace(',', ' ').split(' ')

total_minutes = 0

for time in new_times:
    unit = time[-1]        
    value = int(time[:-1]) 
    
    if unit == 'h':
        minutes = value * 60
    elif unit == 'm':
        minutes = value * 1
    elif unit == 's':
        minutes = value / 60
    
    total_minutes += minutes
print(total_minutes, 'минут')

