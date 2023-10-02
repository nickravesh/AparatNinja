from colorama import Fore
from questionary import text, select, Style
import getPlaylistItems
import getVideoDownloadURL
import checkAvailableQualities
import downloadVideo

# get Aparat playlist url from user
userPlaylistURL = text(message="Enter The Playlist URL:\n",
                       qmark=">",
                       style=Style([('question', 'fg:#cc5454'), ('qmark', 'bold')])).ask()
print("part 1 passed")
# fetch the list of videos inside the given playlist
listOfURLs = getPlaylistItems.get_playlist_items_url(userPlaylistURL)
print("part 2 passed")
# get the first video of the playlist to check for available qualities for it
sampleVideoFromPlaylist = getVideoDownloadURL.get_video_download_url(listOfURLs[0], "144p")
print("part 3 passed")
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