import os
import time
import requests
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains


def get_playlist_items_url(playlistURL: str):
    # Initialize the WebDriver
    driver = webdriver.Firefox()

    # Navigate to the playlist page
    playlist_url = "https://www.aparat.com/playlist/example"
    driver.get(playlist_url)

    # Locate the element with class "playlist-list"
    playlist_list_element = driver.find_element(By.CLASS_NAME, "playlist-list")

    # Extract video URLs from the "playlist-list" element
    playlist_items = playlist_list_element.find_elements(By.CLASS_NAME, "playlist-item")

    playlist_urls = []

    for item in playlist_items:
        # Find the <a> element within each "playlist-item" and extract the href attribute (URL)
        video_link = item.find_element(By.TAG_NAME, "a")
        video_url = video_link.get_attribute("href")
        
        playlist_urls.append(video_url)

    # Print the extracted video URLs
    for url in playlist_urls:
        print(url)

    # Close the WebDriver when done
    driver.quit()


def get_video_url(videoUrl: str, videoQuality: str) -> str:

    # enable the firefox options to set arguments
    firefoxOptions = webdriver.FirefoxOptions()
    firefoxOptions.add_argument("--headless")
    #firefoxOptions.add_argument("--mute-audio")
    #firefoxOptions.add_argument("--no-sandbox")
    #firefoxOptions.add_argument("--disable-dev-shm-usage")
    #firefoxOptions.add_argument('--disable-extensions')
    #firefoxOptions.add_argument('--disable-gpu')
    # set the web driver to firefox
    driver = webdriver.Firefox(options=firefoxOptions)
    # navigate to video page
    driver.get(videoUrl) # sample video: https://www.aparat.com/v/sUzJX
    # wait for the page to load for the maximum of 30 seconds
    driver.implicitly_wait(30)

    # delete all the cookies of the website
    driver.delete_all_cookies()
    # click on the right slider menue of the aparat.com
    aparat_rightMenue = driver.find_element(By.XPATH, '/html/body/div[2]/header/div/div[1]/div[1]/div[1]/button')
    aparat_rightMenue.click()

    # click on the middle of the page just to close the opened menue
    time.sleep(0.2)
    aparat_pageCenter = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[1]')
    aparat_pageCenter.click()

    # scroll down the page a little to load needed content
    #driver.execute_script("window.scrollBy(0, 1000);")
    aparat_rightMenue.send_keys(Keys.PAGE_DOWN)

    # click on the download button of the video
    time.sleep(1.5)
    element3 = driver.find_element(By.CSS_SELECTOR, 'div.dJTScK:nth-child(1) > button:nth-child(1)')
    element3.click()

    # Locate the subscribe element to move the cursor
    elementToHoverOver = driver.find_element(By.CSS_SELECTOR, '.ebyiPU')
    # Create an ActionChains object
    actions = ActionChains(driver)
    # Move the cursor to the specified element without clicking
    actions.move_to_element(elementToHoverOver).perform()

    # Locate the element with the download link (download link needs be extracted from)
    elementContainingDownloadLink = driver.find_element(By.ID, videoQuality) # sample input: '144p'

    # Get the value of the 'href' attribute (or any other attribute containing the link)
    videoDownloadURL = elementContainingDownloadLink.get_attribute("href")

    # Print the link URL for debug
    #print("Link:", videoDownloadURL)

    # Locate the element containing video title
    videoTitleElement = driver.find_element(By.CSS_SELECTOR, ".sc-hKwDye")

    # Get the text content of the <h1> element
    video_title = videoTitleElement.text

    # Print the video title
    print("Video Title:", video_title)    

    # close the driver as its no longer needed
    driver.quit()

    return videoDownloadURL, video_title


def download_video(videoDownloadURL: str, videoTitle: str):
    try:
        response = requests.get(videoDownloadURL, stream=True)
        response.raise_for_status()

        # Check if the file already exists
        if os.path.isfile(f"{videoTitle}.mp4"):
            print(f"The file '{videoTitle}.mp4' already exists.")
            return

        # Get the file size for the progress bar
        videoFileSize = int(response.headers.get('content-length', 0))

        with open(f"{videoTitle}.mp4", "wb") as fileHandler, tqdm(
            desc=f"Downloading {videoTitle}.mp4",
            total=videoFileSize,
            unit_scale=True,
            unit_divisor=1024,
        ) as progressBar:
            for data in response.iter_content(chunk_size=1024):
                fileHandler.write(data)
                progressBar.update(len(data))

        print(f"Download of '{videoTitle}.mp4' complete.")
    except requests.exceptions.HTTPError as e:
        print(f"Failed to download the video: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


download_link = get_video_url(videoUrl='https://www.aparat.com/v/NnJhV', videoQuality='240p')
print(type(download_link))
download_video(download_link[0], download_link[1])

# click on the video download link
# time.sleep(1)
# element4 = driver.find_element(By.CSS_SELECTOR, '.dropdown-content > div:nth-child(1)')
# element4.click()

# time.sleep(0.1)
# element5 = driver.find_element(By.CSS_SELECTOR, '#\31 44p > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)')
# element5.click()

#time.sleep(1)
#element5 = driver.find_element(By.LINK_TEXT, 'با کیفیت 480p')
# element5 = driver.find_element(By.ID, '144p')
# element5.click()

# # Get the current URL and save it to a variable
# pageURL = driver.current_url

# # Print the current URL
# print("Current URL:", pageURL)