from colorama import Fore
from questionary import text, select, Style
import getPlaylistItems
import getVideoDownloadURL
import checkAvailableQualities
import downloadVideo
from utils import loading_animation

print("""
    ___                           __  _   ___         _      
   /   |  ____  ____ __________ _/ /_/ | / (_)___    (_)___ _
  / /| | / __ \/ __ `/ ___/ __ `/ __/  |/ / / __ \  / / __ `/
 / ___ |/ /_/ / /_/ / /  / /_/ / /_/ /|  / / / / / / / /_/ / 
/_/  |_/ .___/\__,_/_/   \__,_/\__/_/ |_/_/_/ /_/_/ /\__,_/  
      /_/                                      /___/         
""")
# get Aparat playlist url from user
userPlaylistURL = text(message="Enter The Playlist URL:\n",
                       qmark=">",
                       style=Style([('question', 'fg:#cc5454'), ('qmark', 'bold')])).ask()

# fetch the list of videos inside the given playlist
loading_animation.show_loading_animation(custom_message="Fetching Playlist Items...")
listOfURLs = getPlaylistItems.get_playlist_items_url(userPlaylistURL)
loading_animation.show_loading_animation(False, custom_message="Fetching Playlist Items...DONE!")
# get the first video of the playlist to check for available qualities for it
sampleVideoFromPlaylist = getVideoDownloadURL.get_video_download_url(listOfURLs[0], "144p")

# get user preferred quality for downloading videos
userSelectedQuality = select(message="In What Quality You Want To Download Videos:",
                             choices=checkAvailableQualities.check_available_qualities(sampleVideoFromPlaylist[0]),
                             pointer=">>",
                             show_selected=True,
                             style=Style([('question', 'fg:#cc5454'),
                                          ('pointer', 'bold'),
                                          ('qmark', 'bold')])).ask()
print("")

#directDownloadLinkWithTitle = []
for item in listOfURLs:
    #directDownloadLinkWithTitle.append(getVideoDownloadURL.get_video_download_url(item, "144p"))
    directDownloadLinkAndVideoTitle = getVideoDownloadURL.get_video_download_url(item, userSelectedQuality)
    downloadVideo.download_video(directDownloadLinkAndVideoTitle[0], directDownloadLinkAndVideoTitle[1])


# TODO: fix firefox webdriver not fully exit in case of an error. fix it with try except that in except in quite the driver