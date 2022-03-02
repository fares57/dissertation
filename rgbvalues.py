from contextlib import redirect_stderr
from genericpath import samefile
from pickle import TRUE
from PIL import ImageColor
from yachalk import chalk
import os

with open('colors.txt', 'r') as f:
    colors = f.readlines()


def sames(red,green,blue):
    if ((abs(abs(red) - abs(green))) <=20) and ((abs(abs(red) - abs(blue))) <=20) and ((abs(abs(green) - abs(blue))) <=20):
        return True
    else:
        return False

def triad_difference(first, second):
    if (abs(first - second)) >=50:
        return True
    else:
        return False

def far_from_borders(red, green, blue):
    if ((red >= 30) or (green >= 30) or (blue >= 30)) and ((red <= 220) or (green <= 220) or (blue <= 220)):
        return True
    else:
        return False

def bigger(first, second):
    if first > second:
        return True
    else:
        return False


global chosen_color
# chosen_color = "#fff200"
chosen_color = ""

def get_rgb(color):
    global red 
    red = 0
    red = ImageColor.getcolor(color, "RGB")[0]
    global green 
    green = 0
    green = ImageColor.getcolor(color, "RGB")[1]
    global blue 
    blue = 0
    blue = ImageColor.getcolor(color, "RGB")[2]

    print(red, green, blue)
    print(sames(red,green,blue))
    print("Red and Green are different by 50:",triad_difference(red,green))
    print("is there at least a color far from borders: ", far_from_borders(red,green,blue))

    if far_from_borders(red, green, blue) and (sames(red,green,blue)):
        # print("grey")
        print(chalk.bg_hex(chosen_color).black("grey"))
    elif ((red < 30) and (green < 30) and (blue < 30)) and (sames(red,green,blue)):
        # print("black")
        print(chalk.bg_hex(chosen_color).black("black"))
    elif ((red > 220) and (green > 220) and (blue > 220)) and (sames(red,green,blue)):
        # print("white")
        print(chalk.bg_hex(chosen_color).black("white"))
    elif far_from_borders(red, green, blue) and (bigger(red, green)) and (bigger(red, blue)) and (triad_difference(red,green)):
        print(chalk.bg_hex(chosen_color).black("red"))
    elif far_from_borders(red, green, blue) and (bigger(green, red)) and (bigger(green, blue)) and (triad_difference(blue, green)):
        print(chalk.bg_hex(chosen_color).black("green"))
    elif far_from_borders(red, green, blue) and (bigger(blue, red)) and (bigger(blue, green)) and (triad_difference(blue, red)) and (triad_difference(blue, green)):
        print(chalk.bg_hex(chosen_color).black("blue"))
    elif far_from_borders(red, green, blue) and (not triad_difference(red, green)) and (bigger(red, blue) or (bigger(green, blue))) and not triad_difference(blue, red) and not triad_difference(blue, green):
        print(chalk.bg_hex(chosen_color).black("yellow"))
    elif far_from_borders(red, green, blue) and (not triad_difference(blue, green)) and (bigger(blue, red) or (bigger(green, red))):
        print(chalk.bg_hex(chosen_color).black("cyan"))-
    elif far_from_borders(red, green, blue) and (not triad_difference(blue, red)) and ((bigger(blue, green)) or (bigger(red, green))):
        print(chalk.bg_hex(chosen_color).black("magenta"))
    else:
        print("not grey")
        print(chalk.bg_hex(chosen_color).black("other"))



for color in colors:
    chosen_color = "#"+color.split('\n')[0]
    try:
        get_rgb(chosen_color)
    except:
        # print('wrong color code')
        continue





