# SlideMatcher

## Inspiration
Our inspiration is the hardship that we felt before the exam night. Fortunately, USC tries very hard to help the students using DEN and make sure everyone can study at their own pace and also can revise at the time of exams. We also get slides for the lectures. But, often times neither alone is sufficient. With slides, we can refer to information very quickly but it could be too dense to interpret without explanation. On the other hand, videos are quite helpful in understanding stuff but can also take hours to parse through. It would be great if we have something by which we can fully integrate visual and auditory learning experience.

## What it does
Slide Matcher is a double-sided mapping between DEN videos and lecture slides to allow seamless transition between the two. We can watch a few slides on our own and when the material gets a little dense we can switch instantly to the exact point in the video where the same concept is being explained. It allows students to navigate between their own class notes, lecture slides and videos with a single click on this platform.

## How we built it
Collected our data by extracting all the lecture slides with PyPDF and high entropy frames from the video using PySceneDetect. After extraction, we ran our matching algorithm which uses Structural Similarity to see how closely each of the frames matches up with slides using Image processing and audio analysis. Using this performance matrix, we identify the optimum video frame for each of the slide using OpenCV and Scikit-image with more than 90% confidence.

## What's next for Slide Matcher
Improve mapping algorithm by also utilizing audio from lectures and text from slides.
