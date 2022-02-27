from contextlib import redirect_stderr
from genericpath import samefile
from pickle import TRUE
from PIL import ImageColor
from yachalk import chalk


global chosen_color
chosen_color = "#03090a"


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

    global same
    if ((abs(abs(red) - abs(green))) <=20) and ((abs(abs(red) - abs(blue))) <=20) and ((abs(abs(green) - abs(blue))) <=20):
        same = 1
    else:
        same = 0

    if ((red >= 30) and (green >= 30) and (blue >= 30)) and ((red <= 220) and (green <= 220) and (blue <= 220)) and (same == 1):
        # print("grey")
        print(chalk.bg_hex(chosen_color).black("grey"))
    elif ((red < 30) and (green < 30) and (blue < 30)) and (same == 1):
        # print("black")
        print(chalk.bg_hex(chosen_color).black("black"))
    elif ((red > 220) and (green > 220) and (blue > 220)) and (same == 1):
        # print("white")
        print(chalk.bg_hex(chosen_color).black("white"))
    else:
        print("not grey")
        print(chalk.bg_hex(chosen_color).black("not grey"))



get_rgb(chosen_color)




