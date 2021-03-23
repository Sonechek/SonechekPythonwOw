from PIL import Image

img = Image.open(r'''c:\Users\alexa\OneDrive\Desktop\SonechekPython\Labs\Semestr_2\Labrab3\1.jpg''')

width, height = img.size

kx = 256 / width
ky = 256 / height

for y in range(height):
    for x in range(width):
        r, g, b = img.getpixel((x,y))
        if r == 12 and g == 12 and b == 12:

            clr = int((kx * y)/2)
        
            r, g, b = clr, clr, clr
            img.putpixel((x, y), (r, g, b))

img.show()