import cv2
from skimage.measure import compare_ssim
import os

image1 = "Images/frame_1.jpg"
image2 = "Pdf_Images/samplelog_jrs0019_p1.png"


def ssim(grayA, grayB):
    imageA = cv2.imread(grayA)
    imageA = cv2.resize(imageA, (1024, 1024))
    imageA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)

    imageB = cv2.imread(grayB)
    imageB = cv2.resize(imageB, (1024, 1024))
    imageB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    (score, diff) = compare_ssim(imageA, imageB, full=True)
    diff = (diff * 255).astype("uint8")
    print("SSIM: {}".format(score))

    return score


print(ssim(image1, image2))

def find_frames():
    Pdf_dir = "Pdf_Images"
    video_dir = "Images"

    print(os.listdir(Pdf_dir))

find_frames()