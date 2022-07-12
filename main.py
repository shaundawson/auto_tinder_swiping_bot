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

def sign_in():
    try:
        sign_in = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a")
        sign_in.click()
        pause()
        fb_login = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]")
        fb_login.click()
        pause()
        #Switch to Facebook login window
        base_window = driver.window_handles[0]
        fb_login_window = driver.window_handles[1]
        driver.switch_to.window(fb_login_window)
        print(driver.title)
        #Login and hit enter
        email = driver.find_element(By.NAME, 'email')
        password = driver.find_element(By.NAME,'pass')
        email.send_keys(EMAIL)
        password.send_keys(PASSWORD)
        pause()
        password.send_keys(Keys.ENTER)
        #Switch back to Tinder window
        driver.switch_to.window(base_window)
        print(driver.title)
        
    except:
       pass
   
sign_in()
pause()

#Allow location
allow_location_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[1]/span')
allow_location_button.click()

#Disallow notifications
notifications_button = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

#Allow cookies
cookies = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

driver.quit()