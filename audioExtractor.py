from moviepy import *

cvt_video = VideoFileClip("Stop Ignoring Me Ignoring You.mp4")

ext_audio = cvt_video.audio

ext_audio.write_audiofile("Dont ignore me.mp3")