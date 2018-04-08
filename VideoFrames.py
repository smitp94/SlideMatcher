import scenedetect
from PIL import Image
import pytesseract
import cv2
import os
from sim import find_frames

frames = []


def keyFrame():
    scene_list = []        # Scenes will be added to this list in detect_scenes().
    path = 'Files/video.mp4'  # Path to video file.

    # Usually use one detector, but multiple can be used.
    detector_list = [
        scenedetect.detectors.ThresholdDetector(threshold=1, min_percent=0.2)
    ]

    video_framerate, frames_read = scenedetect.detect_scenes_file(
        path, scene_list, detector_list)

    # scene_list now contains the frame numbers of scene boundaries.
    print(scene_list)
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

# keyFrame()


def all_frames():
    global frames
    vidcap = cv2.VideoCapture('Files/video.mp4')
    success, image = vidcap.read()
    count = 0
    success = True

    while success:
        success, image = vidcap.read()
        if count%30 == 0:
            cv2.imwrite("Images/frame%d.jpg" % count, image)  # save frame as JPEG file
            frames.append("frame%d.jpg" % count)

        if cv2.waitKey(10) == 27:  # exit if Escape is hit
            break
        count += 1
    # print(frames)

all_frames()
find_frames(frames)

