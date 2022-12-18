from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# LOGIN INFO: minh0608@outlook.com | minh0608
driver = webdriver.Chrome()
driver.get("https://www.quizizz.com/login")

# Login Screen -> Choose Email Option -> Create Quiz Screen
driver.find_element(By.CLASS_NAME, 'email').click()
emailTxt = driver.find_element(By.NAME, "Enter email address or username")
passdTxt = driver.find_element(By.NAME, "Password")
emailTxt.clear()
passdTxt.clear()
emailTxt.send_keys("minh0608@outlook.com")
passdTxt.send_keys("minh0608")
loginScreen = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'continue-button'))
)
driver.find_element(By.CLASS_NAME, 'continue-button').click()

# Keyboard Navigate to Quiz Generate Area
# driver.implicitly_wait(4)
mainScreen = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'admin-external-link'))
)
driver.find_element(By.CLASS_NAME, 'admin-external-link').click()

creatingScreen = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located(
        (By.XPATH, '//*[@id="__layout"]/div/div[3]/main/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/button'))
)
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/main/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/button').click()

# Make a Question
# driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/main/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/button').click()

breakpoint()
