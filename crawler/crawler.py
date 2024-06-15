import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def scrape_music_titles(keyword):
    chrome_options = Options()
    download_dir = "C:\\Users\\aghil\\Downloads"  # Set the path to your download directory

     # Enable headless mode and disable GPU
        #test yanis

    chrome_options.add_experimental_option('prefs', {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get('https://mp3-juices.nu/ajdO/')
        time.sleep(1)

        search_box = driver.find_element(By.NAME, 'query')
        search_box.send_keys(keyword + " audio")
        search_box.send_keys(Keys.RETURN)
        time.sleep(1)

        song = driver.find_element(By.CLASS_NAME, 'result').find_element(By.TAG_NAME, 'a')
        song.click()

        while True:
            if driver.find_element(By.CLASS_NAME, 'result').find_element(By.TAG_NAME, 'a').text != 'Download':
                time.sleep(1)
            else:
                break

        song_completed = driver.find_element(By.CLASS_NAME, 'result').find_element(By.TAG_NAME, 'a')
        song_completed.click()

        # Wait for the download to complete
        while True:
            files = os.listdir(download_dir)
            if any(file.endswith('.crdownload') or file.endswith('.tmp') for file in files):
                print('Download in progress...')
                
                time.sleep(1)
            else:
                break

        print('Download completed:', song_completed.text)

    finally:
        driver.quit()

# Input from the user
inputMan = input("Entrez une musique: ")
scrape_music_titles(inputMan)
