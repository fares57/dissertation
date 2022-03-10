import webcolors
from PIL import ImageColor

def  find_closest_color(rgb_color):
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - rgb_color[0]) ** 2
        gd = (g_c - rgb_color[1]) ** 2
        bd = (b_c - rgb_color[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def find_color_name(rgb_color):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(rgb_color)
    except ValueError:
        closest_name =  find_closest_color(rgb_color)
        actual_name = None
    return actual_name, closest_name

list_ = []

file1 = open('colors.txt', 'r')
Lines = file1.readlines()
count = 0



for line in Lines:
    line = line.strip()
    count += 1
    if line == "Not Accessible":
        list_.append(line)
        continue
    else:

        if len(line) != 6:
            print("given hex value is 5 digit, need 6 digit hex")
            # list_.append("Wrong_color_code")
            continue
        else:
            rgb = ImageColor.getcolor('#'+line, "RGB")
            actual_name, closest_name = find_color_name(rgb)
            list_.append(closest_name)
        print("Line{}: {}, color: {}".format(count, line.strip(),closest_name))

file1.close()

print(len(list_))
print(len(set(list_)))

f = open("color_names.txt", "w")
for item in list_:
    f.write(item+"\n")
f.close()
