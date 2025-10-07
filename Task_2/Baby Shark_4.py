sharks = {}
with open('Baby Shark.txt', encoding='utf-8') as file:
    lines = [line.strip() for line in file if line.strip()]
for i in range(len(lines)):
    line = lines[i]
    if not line.startswith(' '): 
        order = line
        sharks[order] = {}
    elif line.startswith('  ') and not line.lstrip().startswith('   '): 
        family = line.strip()
        sharks[order][family] = {}
    elif line.startswith('  ') and not line.lstrip().startswith('   '): 
        genus = line.strip()
        sharks[order][family][genus] = {}
    else:
        species_line = line.strip()
        if ': ' in species_line:
            species_name, common_name = species_line.split(': ', 1)
            sharks[order][family][genus][species_name] = common_name
print(sharks['Lamniformes']['Lamnidae']['Carcharodon']['C. carcharias'])
    