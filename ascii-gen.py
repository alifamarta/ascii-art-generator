from PIL import Image

# load image
img_flag = True
path = input('Enter the path of the image file: \n')

try:
    img = Image.open(path)
    img_flag = True

    # resize image
    width, height = img.size
    aspect_ratio = height/width
    new_width = 120
    new_height = new_width * aspect_ratio * 0.55
    img = img.resize((new_width, int(new_height)))

    # convert image to grayscale
    img = img.convert('L')

    # list of ASCII characters
    ascii_chars = ["@", "$", "%", "*", "-", "+", "=", "o", ",", "."]

    # convert image to ascii art
    pixels = img.getdata()
    scale = len(ascii_chars) - 1
    new_pixels = [ascii_chars[pixel * scale //255] for pixel in pixels]
    new_pixels = ''.join(new_pixels)

    # split string of chars into multiple string 
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels [index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_image = '\n'.join(ascii_image)
    print(ascii_image)

    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)

except Exception as e:
    print(e)