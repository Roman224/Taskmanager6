from PIL import Image

#. transform image

image = Image.open("Gârlă Eugeniou,dr., profesor de grad superior.pdf")
#image.show()
print("++++++++++++++++")
print(image.size)
print("++++++++++++++++")
new_size = image.resize((400,400))
new_size.show()
new_size.save("ârlă Eugeniou,dr., profesor de grad superio.png")
