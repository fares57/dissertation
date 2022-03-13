from unittest import result
import matplotlib               # data viz


with open('color_names.txt', 'r') as f:
    colors = f.readlines()

    resultsfile = open('./hex_names.txt', 'a')

for color in colors:
    if color.strip('\n') == "Not Accessible":
        resultsfile.write("Not Accessible"+'\n')
    elif color.strip('\n') == "No Image":
        resultsfile.write("No Image"+'\n')
    elif color.strip('\n') == "Wrong_color_code":
        resultsfile.write("Wrong_color_code"+'\n')
    else:
        print(color.strip('\n'))
        resultsfile.write(matplotlib.colors.cnames[color.strip('\n')]+'\n')

f.close()
resultsfile.close()

