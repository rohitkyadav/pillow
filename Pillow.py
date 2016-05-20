from PIL import Image

rohit = Image.open("Rohit.jpg")
rohit1 = Image.open("alien2.png")

r1, g1, b1 = rohit.split()
r2, g2, b2 = rohit1.split()

new_img = Image.merge("RGB", (r2, g1, b2))
new_img.show()
