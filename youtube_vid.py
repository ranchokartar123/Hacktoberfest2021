import pytube  
from pytube import YouTube
import os
video_url = str(input("enter youtube video url:"))
youtube = pytube.YouTube(video_url)  
video = youtube.streams.first()  
video.download('C:/Users/+'+os.getlogin()'+/Downloads')  
