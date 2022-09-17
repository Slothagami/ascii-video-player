from playsound import playsound
from ascii_image import Charmap
import ascii_video

video = "videos/bad_apple"

playsound(video + ".mp3", False)
ascii_video.display(video + ".mp4", map=Charmap.simple)