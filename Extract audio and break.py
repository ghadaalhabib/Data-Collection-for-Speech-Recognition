#!/usr/bin/env python
# coding: utf-8



from moviepy.editor import *
import os
def extract_audio(video_file):
        # Load the video file and extract the audio
        video = VideoFileClip(video_file)
        audio = video.audio
    
        # Create a directory to store the audio files
        audio_dir = os.path.splitext(video_file)[0] + '_audio'
        if not os.path.exists(audio_dir):
            os.makedirs(audio_dir)
    
        # Split the audio into 1 minute batches and save them to disk
        duration = audio.duration
        for i, t in enumerate(range(0, int(duration), 60)):
            batch = audio.subclip(t, t+60)
            batch_file = os.path.join(audio_dir, f'{i+1}.mp3')
            batch.write_audiofile(batch_file)
    
        # Close the video file and return the directory path
        video.close()
        return audio_dir
    





