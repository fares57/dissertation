from asyncio.windows_events import NULL
import webbrowser

with open('links.txt', 'r') as f:
    myNames = f.readlines()

def detect_text_uri(uri):
    """Detects text in the file located in Google Cloud Storage or on the Web.
    """
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

for index, name in enumerate(myNames):
    print('iteration: ', index + 1, ' of: ', len(myNames))
    try:
        detect_text_uri(str(name))
        webbrowser.open(str(name))
        print('\n')
    except:
        print('Not Accessible', '\n')
        pass
