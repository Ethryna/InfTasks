from moviepy.editor import *
import os
directory = 'C:/Users/student/Documents/142Б'
files = os.listdir(directory)
print(files)
images = list(filter(lambda x: x.endswith('.jpg'), files))
clips = [ImageClip(m).set_duration(2) for m in images]
final_clip = concatenate_videoclips(clips, method='compose')
final_clip.write_videofile('Quotes.mp4', fps = 24)