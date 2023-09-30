from colorama import Fore
import getPlaylistItems
import getVideoDownloadURL
import downloadVideo

# get playlist items url
userPlaylistURL = input(f"{Fore.LIGHTMAGENTA_EX}Enter The Playlist URL:{Fore.RESET}\n")
userSelectedQuality = input(f"{Fore.LIGHTYELLOW_EX}Enter The Quality You Want To Download Videos:{Fore.RESET}\n")
listOfURLs = getPlaylistItems.get_playlist_items_url(userPlaylistURL)

directDownloadLinkWithTitle = []
for item in listOfURLs:
    #directDownloadLinkWithTitle.append(getVideoDownloadURL.get_video_download_url(item, "144p"))
    directDownloadLinkAndVideoTitle = getVideoDownloadURL.get_video_download_url(item, userSelectedQuality)
    downloadVideo.download_video(directDownloadLinkAndVideoTitle[0], directDownloadLinkAndVideoTitle[1])



# TODO: fix firefox webdriver not fully exit in case of an error. fix it with try except that in except in quite the driver