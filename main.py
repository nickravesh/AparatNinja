import downloadVideo
import getPlaylistItems
from colorama import Fore
import getVideoDownloadURL
import checkAvailableQualities
from utils import loading_animation
from questionary import text, select, Style

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

# fetch the list of videos inside the given playlist and the playlist name
loading_animation.show_loading_animation(custom_message="Fetching Playlist Items...")
listOfURLs, playlistName = getPlaylistItems.get_playlist_items_url(userPlaylistURL)
loading_animation.show_loading_animation(False, custom_message="Fetching Playlist Items...DONE!")

# get the first video of the playlist to check for available qualities for it
loading_animation.show_loading_animation(custom_message="Checking Available Video Qualities...")
sampleVideoFromPlaylist = getVideoDownloadURL.get_video_download_url(listOfURLs[0], "144p")
loading_animation.show_loading_animation(False, custom_message="Checking Available Video Qualities...DONE!")

# test the possible qualities and see if they are valid
loading_animation.show_loading_animation(custom_message="Validating The Available Qualities, just for you!")
validChoices = checkAvailableQualities.check_available_qualities(sampleVideoFromPlaylist[0])
loading_animation.show_loading_animation(False, custom_message="Validating The Available Qualities...DONE!")

# get user preferred quality for downloading videos
userSelectedQuality = select(message="In What Quality You Want To Download Videos:",
                             choices=validChoices,
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
    downloadVideo.download_video(directDownloadLinkAndVideoTitle[0], directDownloadLinkAndVideoTitle[1], playlistName)
