# sea_fish = ["shark", "flounder", "tuna", "cod", "herring", "Marlin"]
# freshwater_fish = ["Asp", "Pike", "Carp", "Salmon", "Ide", "Trout"]

# all_fish = sea_fish + freshwater_fish

# n = len(all_fish)
# for i in range(n):
#     for j in range(0, n-i-1):
#         if all_fish[j].lower() > all_fish[j+1].lower():
#             all_fish[j], all_fish[j+1] = all_fish[j+1], all_fish[j]
# print(all_fish)

s = ["shark", "flounder", "tuna", "cod", "herring", "Marlin"]
f = ["Asp", "Pike", "Carp", "Salmon", "Ide", "Trout"]
a = sorted(s + f, key=lambda x: x.lower())
print(a)