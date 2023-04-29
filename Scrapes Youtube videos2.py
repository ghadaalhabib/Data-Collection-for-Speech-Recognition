import requests
from bs4 import BeautifulSoup
import json
import re

def scrape_video_info(videoList):
    """
    Scrape video information from a list of YouTube video URLs.

    Args:
        videoList (list): A list of YouTube video URLs.

    Returns:
        None. Prints the following information for each video:
            - Title
            - Description
            - Tags
            - Length
            - Channel Name
            - Upload Date
    """
    for index, url in enumerate(videoList):
        # Send a GET request to the URL and retrieve the HTML content
        response = requests.get(url)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract the JSON data containing video information from the HTML content
        json_data = ''
        for script in soup.find_all('script'):
            if 'ytInitialPlayerResponse' in str(script):
                json_data = str(script)
                break

        # Extract the video information from the JSON data using regular expressions    
        pattern = re.compile(r'ytInitialPlayerResponse\s*=\s*({.*?});', flags=re.DOTALL)
        match = pattern.search(json_data)
        if match:
            json_str = match.group(1)   
            data = json.loads(json_str)
            # Video title
            title = data['videoDetails']['title']
            # Description text
            description = data['videoDetails']['shortDescription']
            # Video tags
            tags = data['videoDetails']['keywords']
            # Video length
            length = data['videoDetails']['lengthSeconds']
            # Channel name
            channel_name = data['videoDetails']['author']
            # Upload date
            upload_date = data['microformat']['playerMicroformatRenderer']['publishDate']
