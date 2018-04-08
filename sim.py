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
    # print("SSIM: {}".format(score))

    return score


# print(ssim(image1, image2))

def find_frames(frames):
    Pdf_dir = "Pdf_Images"
    video_dir = "Images"

    Pdfs = os.listdir(Pdf_dir)
    # frames = os.listdir(video_dir)
    # frames.sort()
    mapping = {}

    # for page in Pdfs:
    #     max = 0
    #     vid = ""
    #     pdf = ""
    i=0
    for frame in frames:
        s = ssim(Pdf_dir + "/" + Pdfs[i], video_dir + "/" + frame)
        # if max < s:
        if s > 0.85:
            max = s
            pdf = Pdfs[i]
            i += 1
            vid = frame
            mapping[pdf] = int(vid[5:-4])*15
            print(pdf)
            if i > len(Pdfs)-1:
                break

    print(mapping)


# find_frames()
