from contextlib import redirect_stderr
from genericpath import samefile
from pickle import TRUE
from PIL import ImageColor
from yachalk import chalk


global chosen_color
chosen_color = "#1e2db0"


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
    elif ((red >= 30) and (green >= 30) and (blue >= 30)) and ((red <= 220) and (green <= 220) and (blue <= 220)) and (red > green) and (red > blue):
        print(chalk.bg_hex(chosen_color).black("red"))
    elif ((red >= 30) and (green >= 30) and (blue >= 30)) and ((red <= 220) and (green <= 220) and (blue <= 220)) and (green > red) and (green > blue):
        print(chalk.bg_hex(chosen_color).black("green"))
    elif ((red >= 30) and (green >= 30) and (blue >= 30)) and ((red <= 220) and (green <= 220) and (blue <= 220)) and (blue > red) and (blue > green):
        print(chalk.bg_hex(chosen_color).white("blue"))
    elif ((red >= 30) and (green >= 30) and (blue >= 30)) and ((red <= 220) and (green <= 220) and (blue <= 220)) and (blue > red) and (blue > green):
        print(chalk.bg_hex(chosen_color).white("blue"))    
    else:
        print("not grey")
        print(chalk.bg_hex(chosen_color).black("not grey"))



get_rgb(chosen_color)




