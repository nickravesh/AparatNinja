from selenium import webdriver
from selenium.webdriver.common.by import By

def get_playlist_items_url(playlistURL: str) -> list:

    firefoxOptions = webdriver.FirefoxOptions()
    firefoxOptions.add_argument("--headless")

    # Initialize the WebDriver
    driver = webdriver.Firefox(options=firefoxOptions)

    # Navigate to the playlist page
    driver.get(playlistURL)

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

    return playlist_urls


# usage:
#get_playlist_items_url("https://www.aparat.com/playlist/example")

# TODO: store the extracted urls in a list