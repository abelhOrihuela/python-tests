from imutils import paths

print("[INFO] loading images...")
imagePaths = sorted(list(paths.list_images("images")))
images = []


for imagePath in imagePaths:
	image = cv2.imread(imagePath)
	images.append(image)
# initialize OpenCV's image sticher object and then perform the image
# stitching
print("[INFO] stitching images...")
stitcher = cv2.createStitcher() if imutils.is_cv3() else cv2.Stitcher_create()
(status, stitched) = stitcher.stitch(images)
