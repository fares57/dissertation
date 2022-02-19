from asyncio.windows_events import NULL
import webbrowser
import os
import sys
import requests
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import urllib.request

font = ImageFont.truetype("Amble-Regular.ttf", 30)


with open('links.txt', 'r') as f:
    myNames = f.readlines()

def detect_faces_uri(uri):
    global results
    global faces_number
    """Detects faces in the file located in Google Cloud Storage or the web."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri

    response = client.face_detection(image=image)
    faces = response.face_annotations



    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    print('Faces:' + str(len(faces)))
    faces_number = str(len(faces))
    results = []
    for index3, face in enumerate(faces):
        print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
        print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
        print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))
        print('Sorrow: {}'.format(likelihood_name[face.sorrow_likelihood]))

        results.append([])
        
        results[index3] = ['anger: {}'.format(likelihood_name[face.anger_likelihood]),
        'joy: {}'.format(likelihood_name[face.joy_likelihood]),
        'surprise: {}'.format(likelihood_name[face.surprise_likelihood]),
        'Sorrow: {}'.format(likelihood_name[face.sorrow_likelihood])
        ]
        

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in face.bounding_poly.vertices])

        print('face bounds: {}'.format(','.join(vertices)))
    
    print(len(results), " ", list(results))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

for index, name in enumerate(myNames):
    print('iteration: ', index + 1, ' of: ', len(myNames))
    resultsfile = open('./results.csv', 'a')
    try:
        detect_faces_uri(str(name))
        # webbrowser.open(str(name))
        
        f = open('./images/image'+str(index+1)+'.jpg','wb')
        f.write(urllib.request.urlopen(str(name)).read())
        f.close()

        print("download successful")

        img = Image.open('./images/image'+str(index+1)+'.jpg')
        I1 = ImageDraw.Draw(img)
        resultsfile.write(name + "," + faces_number + ",")
        I1.text((0, 0), str(faces_number), fill=(255, 0, 0), font=font)
        for index2, result in enumerate(results):
            for index4, innerresult in enumerate(result):
                I1.text((0, 30 + index4 * 30 + index2 * 130), str(innerresult), fill=(255, 0, 0), font=font)
            resultsfile.write(str(result) + ", ")
        resultsfile.write("\n")
        img.save('./images/image'+str(index+1)+'.jpg')

    except:
        print('Not Accessible', '\n')
        resultsfile.write(name + ",")
        resultsfile.write("," + "Not Accessible")
        resultsfile.write("\n")
        pass

    resultsfile.close()
