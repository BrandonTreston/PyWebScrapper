import re
regex_example = "a timeless classic, our 100% cotton sweater 12% pp 44% poopoo fabric is essential for leather 80% layering."

# print(re.findall('\d{1,3}% \w+', regex_example))
materials = ['cotton', 'poopoo', 'leather', 'coom', 'sloot']
for material in materials:
    percentage = re.findall( '\d+\D (?=' + material + ')', regex_example)
    if percentage:
        print(percentage[0])
    
    else:
        print('n/a')

    