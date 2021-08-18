from PIL import Image

inputs = ['./outputs/StarryNight_font.png',
          './outputs/StarryNight_circles.png',
          './outputs/StarryNight_lines.png']

IMAGE_WIDTH = 512
IMAGE_HEIGHT = 512

image = Image.new('RGBA', (IMAGE_WIDTH * len(inputs), IMAGE_HEIGHT), (0, 0, 0, 255))

for i in range(len(inputs)):
    sub_image = Image.open(inputs[i])
    image.paste(sub_image, (i * IMAGE_WIDTH, 0), sub_image)

image.save('collage.png')
