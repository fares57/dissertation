from asyncio.windows_events import NULL
import webbrowser
import os
import sys
import requests
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import urllib.request


with open('links.txt', 'r') as f:
    myNames = f.readlines()


def rgb_to_hex(r, g, b):
  return ('{:X}{:X}{:X}').format(r, g, b)

def detect_properties_uri(uri):
    """Detects image properties in the file located in Google Cloud Storage or
    on the Web."""
    global result
    result = []
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri


    response = client.image_properties(image=image)
    props = response.image_properties_annotation
    for index2, color2 in enumerate(props.dominant_colors.colors):
        result.append([])
        hex = rgb_to_hex(int(color2.color.red), int(color2.color.green), int(color2.color.blue))
        result[index2] = [hex, color2.score]
    print('Score is: ', result)
    print('Properties:')

    for color in props.dominant_colors.colors:
        print('frac: {}'.format(color.pixel_fraction))
        print('Score: {}'.format(color.score))
        print('\tr: {}'.format(color.color.red))
        print('\tg: {}'.format(color.color.green))
        print('\tb: {}'.format(color.color.blue))
        print('\ta: {}'.format(color.color.alpha))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))


for index, name in enumerate(myNames):
    print('iteration: ', index + 1, ' of: ', len(myNames))
    resultsfile = open('./imageresults.xls', 'a')
    try:
        detect_properties_uri(str(name))
        print('\n')
        # resultsfile.write(str(name))
        resultsfile.write(str(name) + '*' + str(result) + '\n')
        # resultsfile.write("\n")
        # resultsfile.writelines("")
        # for index3, result in enumerate(results):
        #     resultsfile.write(str(result))
        # resultsfile.write("\n")
    except:
        print('Not Accessible', '\n')
        resultsfile.write(str(name) + '*' + "Not Accessible" + "\n")
        pass
    resultsfile.close()