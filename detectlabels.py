from asyncio.windows_events import NULL
import webbrowser

with open('links.txt', 'r') as f:
    myNames = f.readlines()

def detect_labels_uri(uri):
    """Detects labels in the file located in Google Cloud Storage or on the
    Web."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        print(label.description)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

for index, name in enumerate(myNames):
    print('iteration: ', index + 1, ' of: ', len(myNames))
    try:
        detect_labels_uri(str(name))
        webbrowser.open(str(name))
        print('\n')
    except:
        print('Not Accessible', '\n')
        pass

