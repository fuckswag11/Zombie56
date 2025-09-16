m = float(input("введите растояние в м :"))
km = float(input("введите растояние в kм :"))
mkm = km * 1000
if mkm < m: print('км ', km)
else: print('метры', m)