import os
from pytube import YouTube

def download_URL_from_youtube(file_path):
    # Read the text file
    videoList = [x.strip() for x in open(file_path).readlines()]

    # Create a directory to store the downloaded videos
    download_path = 'YouTube_videos'
    os.makedirs(download_path, exist_ok=True)

    for index, video in enumerate(videoList):
        # Create YouTube object and set highest quality video
        yt = YouTube(video)
        video = yt.streams.get_highest_resolution()

        # Set download path and filename
        filename = yt.title + '.mp4'

        # Download the video
        video.download(download_path, filename)
