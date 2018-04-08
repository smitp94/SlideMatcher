import subprocess
import os
import speech_recognition as sr
# from tqdm import tqdm
from multiprocessing.dummy import Pool
import sys

def audio_conversion():
    files_list = ['Files/soundvideo.mp4']

    for file_num, file_path_input in enumerate(files_list, start=1):
        # Get the file name withoutextension
        file_name = os.path.basename(file_path_input)
        if 'mouthcropped' not in file_name:
            raw_file_name = os.path.basename(file_name).split('.')[0]
            file_dir = os.path.dirname(file_path_input)
            file_path_output = file_dir + '/' + raw_file_name + '.wav'
            print('processing file: %s' % file_path_input)
            subprocess.call(
                ['ffmpeg', '-i', file_path_input, '-codec:a', 'pcm_s16le', '-ac', '1', file_path_output])
            print('file %s saved' % file_path_output)


pool = Pool(8)  # Number of concurrent threads

with open("Files/api-key.json") as f:
    GOOGLE_CLOUD_SPEECH_CREDENTIALS = f.read()

r = sr.Recognizer()
files = os.listdir('Files/sound/parts/')


def transcribe(data):
    idx, file = data
    name = "Files/sound/parts/" + file
    print(name + " started")
    # Load audio file
    with sr.AudioFile(name) as source:
        audio = r.record(source)
    # Transcribe audio file
    text = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
    print(name + " done")
    return {
        "idx": idx,
        "text": text
    }


all_text = pool.map(transcribe, enumerate(files))
pool.close()
pool.join()

transcript = ""
for t in sorted(all_text, key=lambda x: x['idx']):
    total_seconds = t['idx'] * 30
    # Cool shortcut from:
    # https://stackoverflow.com/questions/775049/python-time-seconds-to-hms
    # to get hours, minutes and seconds
    m, s = divmod(total_seconds, 60)
    h, m = divmod(m, 60)

    # Format time as h:m:s - 30 seconds of text
    transcript = transcript + "{:0>2d}:{:0>2d}:{:0>2d} {}\n".format(h, m, s, t['text'])

print(transcript)

with open("Files/transcript.txt", "w") as f:
    f.write(transcript)

