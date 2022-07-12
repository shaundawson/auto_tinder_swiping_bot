import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import random
from keys import CHROME_BINARY_LOC, CHROME_DRIVER_PATH, CHROME_PROFILE_PATH, EMAIL, PASSWORD
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

url="https://tinder.com/"

def pause():
    time_break = random.randint(4,9)
    return time.sleep(time_break)


s=Service(executable_path=CHROME_DRIVER_PATH)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-data-dir={CHROME_PROFILE_PATH}")
chrome_options.binary_location=(CHROME_BINARY_LOC)
driver = webdriver.Chrome(service=s, options=chrome_options)
wait = WebDriverWait(driver, 10)
driver.maximize_window()
driver.get(url)
pause()

# Store the ID of the original window
original_window = driver.current_window_handle
# Check we don't have other windows open already
assert len(driver.window_handles) == 1


def sign_in():
    try:
        sign_in = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a")
        sign_in.click()
        pause()
        fb_login = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]")
        fb_login.click()
        pause()
    except:
       pass
   
sign_in()
pause()
driver.quit()