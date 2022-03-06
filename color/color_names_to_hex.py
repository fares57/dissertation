import matplotlib               # data viz


with open('color_names.txt', 'r') as f:
    colors = f.readlines()

    resultsfile = open('./hex_names.txt', 'a')

for color in colors:
    print(color.strip('\n'))
    resultsfile.write(matplotlib.colors.cnames[color.strip('\n')]+'\n')

