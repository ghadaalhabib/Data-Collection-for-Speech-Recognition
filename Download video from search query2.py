from pytube import YouTube
from pytube import Search
import os

def Download_first_videos_based_on_search_query(search_query):
    
    # Search for videos related to the search query
    results = Search(search_query).results
    
    if not results:
        print('No videos found for the search query.')
    else:
        # Create a directory to store the downloaded videos
        os.makedirs('YouTube_videos', exist_ok=True)
        
        # Download the first 10 videos
        for i, result in enumerate(results[:10]):
            try:
                # Get YouTube object
                yt = YouTube(result.watch_url)
                
                # Get highest resolution stream
                stream = yt.streams.get_highest_resolution()
                
                # Download video
                stream.download(output_path='YouTube_videos')
                
                # Print status
                print(f'Downloaded video {i+1}: {yt.title}')
                
            except Exception as e:
                print(f'Error downloading video: {result.title}.
