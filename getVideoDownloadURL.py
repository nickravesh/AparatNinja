import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains


def get_video_download_url(videoUrl: str, videoQuality: str) -> tuple:

    # enable the firefox options to set arguments
    firefoxOptions = webdriver.FirefoxOptions()
    firefoxOptions.add_argument("--headless")
    firefoxOptions.add_argument("--mute-audio")
    #firefoxOptions.add_argument("--no-sandbox")
    #firefoxOptions.add_argument("--disable-dev-shm-usage")
    firefoxOptions.add_argument('--disable-extensions')
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
    time.sleep(0.5)
    aparat_pageCenter = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[1]')
    aparat_pageCenter.click()

    # scroll down the page a little to load needed content
    #driver.execute_script("window.scrollBy(0, 1000);")
    aparat_rightMenue.send_keys(Keys.PAGE_DOWN)

    # click on the download button of the video
    time.sleep(2)
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


# usage:
# download_link_and_video_title = get_video_download_url(videoUrl='https://www.aparat.com/v/NnJhV', videoQuality='240p')
# print(download_link_and_video_title)