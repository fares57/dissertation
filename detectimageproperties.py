from asyncio.windows_events import NULL
import webbrowser

with open('links.txt', 'r') as f:
    myNames = f.readlines()


def detect_properties_uri(uri):
    """Detects image properties in the file located in Google Cloud Storage or
    on the Web."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri

    response = client.image_properties(image=image)
    props = response.image_properties_annotation
    print('Properties:')

    for color in props.dominant_colors.colors:
        print('frac: {}'.format(color.pixel_fraction))
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
    try:
        detect_properties_uri(str(name))
        webbrowser.open(str(name))
        print('\n')
    except:
        print('Not Accessible', '\n')
        pass