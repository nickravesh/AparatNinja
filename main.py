import getPlaylistItems
import getVideoDownloadURL
import downloadVideo

# get playlist items url
userPlaylistURL = input("Provide PlaylistURL:")
listOfURLs = getPlaylistItems.get_playlist_items_url(userPlaylistURL)

directDownloadLinkWithTitle = []
for item in listOfURLs:
    print("found a video:")
    print(item)

    #directDownloadLinkWithTitle.append(getVideoDownloadURL.get_video_download_url(item, "144p"))
    downloadLink_videoTitle = getVideoDownloadURL.get_video_download_url(item, "144p")
    downloadVideo.download_video(downloadLink_videoTitle[0], downloadLink_videoTitle[1])