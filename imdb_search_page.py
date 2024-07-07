import os
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
paths = r"C:\Users\Ranga\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.imdb.com/search/name/")
driver.maximize_window()
driver.implicitly_wait(60)
try:
    search_box = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'suggestion-search')))
    search_box.send_keys("Aadhya Anand")
    search_button = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="suggestion-search-button"]')))
    search_button.click()
except NoSuchElementException as e:
    print("Error")

except Exception as e:
# Handle other exceptions (TimeoutException, WebDriverException, etc.)
    print(f"An error occurred: {e}")

finally:
    driver.quit()


