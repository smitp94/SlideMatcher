import scenedetect
from PIL import Image
import pytesseract
import cv2
import os


def keyFrame():
    scene_list = []        # Scenes will be added to this list in detect_scenes().
    path = 'Files/ctest.mp4'  # Path to video file.

    # Usually use one detector, but multiple can be used.
    detector_list = [
        scenedetect.detectors.ThresholdDetector(threshold=100, min_percent=0.9)
    ]

    video_framerate, frames_read = scenedetect.detect_scenes_file(
        path, scene_list, detector_list)

    # scene_list now contains the frame numbers of scene boundaries.
    # print(scene_list)
    for frame_no in scene_list:
        cap = cv2.VideoCapture(path)  # video_name is the video being called
        cap.set(1,frame_no);  # Where frame_no is the frame you want
        ret, frame = cap.read()  # Read the frame
        # cv2.imshow('window_name', frame)
        cv2.imwrite("Images/"+"frame"+"_" + str(frame_no) + ".jpg", frame)


def ocr():
    path = "test/"
    file_name = "screen.png"
    file_OCR = path + file_name
    image = cv2.imread(file_OCR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    filename = "test/{}1.png".format(file_name)
    cv2.imwrite(filename, gray)

    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    print(text)
    return text

keyFrame()
