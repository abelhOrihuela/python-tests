from imutils import paths
import cv2
import imutils

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


if status == 1:
	# write the output stitched image to disk
	cv2.imwrite("output.png", stitched)
	# display the output stitched image to our screen
	cv2.imshow("Stitched", stitched)
	cv2.waitKey(0)
# otherwise the stitching failed, likely due to not enough keypoints)
# being detected
else:
	print("[INFO] image stitching failed ({})".format(status))
