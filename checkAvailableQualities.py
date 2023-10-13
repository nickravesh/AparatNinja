import re
import utils
import requests
from colorama import Fore

def check_available_qualities(directDownloadURL: str) -> list:
    allPossibleQualities = []
    choices = ["144p", "240p", "320p", "360p", "480p", "720p", "1080p"] # TODO: expand the quality list
    for item in choices:
        allPossibleQualities.append(directDownloadURL.replace("144p", item))

    try:
        validQualities = []
        for url in allPossibleQualities:
            if requests.get(url, stream=True).status_code == 200:
                validQualities.append(url)
            else:
                #print(f"the URL {url[50]} has discarded")
                pass
    except:
        utils.loading_animation.show_loading_animation(False, custom_message=f"{Fore.LIGHTRED_EX}Unable to connect, Please check your internet connection{Fore.RESET}")
        return exit()

    validQualitiesTags = []
    for url in validQualities:
        validQualitiesTags.append(re.search("\d+p", url).group(0))


    return validQualitiesTags

