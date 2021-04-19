from imutils import paths

print("[INFO] loading images...")
imagePaths = sorted(list(paths.list_images("images")))
images = []
