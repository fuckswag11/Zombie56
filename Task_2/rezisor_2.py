def get_resistor_value (s):
    g1_2 = {'bk' : 0, 'br' : 1,'rd': 2, 'or' : 3, 'yl': 4, 'gr' : 5,
        'bl': 6, 'vi': 7, 'gy' : 8, 'wh' : 9}
    g3 = {'bk' : 1, 'br' : 10,'rd': 100, 'or' : 100, 'yl': 10**4,
      'gr' : 10**5, 'bl': 10**6, 'vi': 10**7, 'gy' : 10**8, 'wh' : 10**9}
    g4 = {'bk' : '-', 'br' : 1,'rd': 2, 'or' : '-', 'yl': 5, 'gr' : 0.5, 
      'bl': 0.25, 'vi': 0.1, 'gy' : 0.05, 'wh' : 1, 'au' : 5, 'ag' : 10, '-' : 20}
    if len(s) < 4 or len(s) > 4:
        print(f'Unidentified or invalid band colour in bands: {s}')
        return (None, None)
    s1, ss1, sss1, ssss1 = s 
    if s1 not in g1_2 or ss1 not in g1_2 or sss1 not in g3 or ssss1 not in g4:
        print(f'Fewer than four colours provided in bands:  {s}')
        return (None, None)
    val1 = g1_2[ s[0] ] #->g1_2['br] -> 1
    val2 = g1_2[ s[1] ]
    val3 = g3[ s[2] ]
    val4 = g4[ s[3] ]
    n = int(str(val1) + str(val2)) * val3, val4
    return n
print(get_resistor_value(['ws', 'yl', 'rd', 'rd']))


    