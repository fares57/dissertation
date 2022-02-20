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

def detect_text_uri(uri):
    """Detects text in the file located in Google Cloud Storage or on the Web.
    """
    global results
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')
    results = []
    if texts == []:
        print('no texts')
        results = ['notext']
    for index2, text in enumerate(texts):
        # print(text.description)
        results.append([])
        results[index2] = text.description
        # vertices = (['({},{})'.format(vertex.x, vertex.y)
        #             for vertex in text.bounding_poly.vertices])

        #print('bounds: {}'.format(','.join(vertices)))
    print(list(results))
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

for index, name in enumerate(myNames):
    print('iteration: ', index + 1, ' of: ', len(myNames))
    resultsfile = open('./textresults.xls', 'a')
    try:
        detect_text_uri(str(name))
        print('\n')
        # resultsfile.write(str(name))
        resultsfile.write(str(name) + '*' + results[0].replace('\n', ' ') + '\n')
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
