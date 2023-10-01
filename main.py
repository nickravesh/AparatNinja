from colorama import Fore
from questionary import text, select, Style
import getPlaylistItems
import getVideoDownloadURL
import downloadVideo

# get Aparat playlist url from user
userPlaylistURL = text(message="Enter The Playlist URL:\n",
                       qmark=">",
                       style=Style([('question', 'fg:#cc5454'), ('qmark', 'bold')])).ask()

# get user preferred quality for downloading videos
userSelectedQuality = select(message="In What Quality You Want To Download Videos:",
                             choices=["144p", "240p", "360p", "480p", "720p", "1080p"],
                             pointer=">>",
                             show_selected=True,
                             style=Style([('question', 'fg:#cc5454'),
                                          ('pointer', 'bold'),
                                          ('qmark', 'bold')])).ask()


listOfURLs = getPlaylistItems.get_playlist_items_url(userPlaylistURL)

directDownloadLinkWithTitle = []
for item in listOfURLs:
    #directDownloadLinkWithTitle.append(getVideoDownloadURL.get_video_download_url(item, "144p"))
    directDownloadLinkAndVideoTitle = getVideoDownloadURL.get_video_download_url(item, userSelectedQuality)
    downloadVideo.download_video(directDownloadLinkAndVideoTitle[0], directDownloadLinkAndVideoTitle[1])



# TODO: fix firefox webdriver not fully exit in case of an error. fix it with try except that in except in quite the driver