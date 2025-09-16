def race(v1, v2, g):
    if v1 >= v2:
        return None
    
    t = g / (v2 - v1)
    
    hours = int(t)
    minutes = int((t - hours) * 60)
    seconds = int(((t - hours) * 60 - minutes) * 60)
    
    return [hours, minutes, seconds]

print(race(720, 850, 70))