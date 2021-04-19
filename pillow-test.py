import requests
from io import BytesIO
from PIL import Image
print("Loading...")

r = requests.get(
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdTVs68M5e7_aK_r7FpdY5dw2AaxGqb2JgR-ld4FXIsQUMIAPG&s")

print("Status code", r.status_code)

image = Image.open(BytesIO(r.content))

print("Size", image.size)
print("Format", image.format)
print("Mode", image.mode)

path = "image." + image.format

try:
  image.save(path, image.format)
except IOError:
  print("Cannot save image")
