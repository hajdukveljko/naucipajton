from PIL import Image, ImageDraw

im = Image.open('IMG_1455.jpg')
pix = im.load()
pix_val = list(im.getdata())
histogram = []

for i in range (0, 256):
    histogram.append(0)
for r,g,b in pix_val:
    histogram[r] += 1
# print(histogram)

max_val = 0
for pix in histogram:
    if pix > max_val:
        max_val = pix
# print(max_val)

im_size_x = 256
im_size_y = 256
hist = Image.new('RGB', (im_size_x, im_size_y), (225,225,225))
draw = ImageDraw.Draw(hist)

x = 0
for val in histogram:
    y = im_size_y - (val*im_size_y/max_val)
    draw.line((x,im_size_y,x,y), fill=255)
    x += 1
hist.show()
