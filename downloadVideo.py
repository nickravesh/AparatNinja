import os
import requests
from tqdm import tqdm


def download_video(videoDownloadURL: str, videoTitle: str, playlistName: str):
    try: # create directory based on playlist name to save videos in it
        if os.path.exists("Downloads") == False:
            os.mkdir("Downloads")
        os.mkdir(f"Downloads/{playlistName}")
    except:
        pass

    try:
        response = requests.get(videoDownloadURL, stream=True)
        response.raise_for_status()

        # Check if the file already exists
        if os.path.isfile(f"Downloads/{playlistName}/{videoTitle}.mp4"):
            print(f"The file '{videoTitle}.mp4' already exists.")
            return

        # Get the file size for the progress bar
        videoFileSize = int(response.headers.get('content-length', 0))
        print(f"Video Title: {videoTitle}.mp4")
        with open(f"Downloads/{playlistName}/{videoTitle}.mp4", "wb") as fileHandler, tqdm(
            #desc=f"Downloading {videoTitle}.mp4",
            desc=f"Downloading...",
            total=videoFileSize,
            unit_scale=True,
            unit_divisor=1024,
            unit="B",
        ) as progressBar:
            for data in response.iter_content(chunk_size=1024):
                fileHandler.write(data)
                progressBar.update(len(data))

        #print(f"Download of '{videoTitle}.mp4' complete.")
        print(f"Download of '{videoTitle[0:25]}...' complete.")
    except requests.exceptions.HTTPError as e:
        print(f"Failed to download the video: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


# usage:
#download_video(download_link_and_video_title[0], download_link_and_video_title[1])
#download_video(videoDownloadURL="https://example.com/files/video.mp4", videoTitle="sampleVideo")