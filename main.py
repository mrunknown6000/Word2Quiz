from utils import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as exc

# FORMAT_TEST = r'C:\Users\admin\.src-code\python\Word2Quiz\content\scan-formatstyle.docx'
LINE_TEST = r'C:\Users\admin\.src-code\python\Word2Quiz\content\scan-linebyline.docx'
TABLE_TEST = r'C:\Users\admin\.src-code\python\Word2Quiz\content\scan-table.docx'
GEO_CASE = r'C:\Users\admin\.src-code\python\Word2Quiz\content\testcasegeo.docx'

# Networking Configuration
driver = webdriver.Chrome()


def main(doc_dir):
    # Initializing All Necessary Resources
    currentDocxString = convertDoc2Txt(doc_dir)
    currentDocxString = filterer(currentDocxString)
    finalizedDictionary = questionIdentification(currentDocxString)

    # WWW Connection Initializing
    driver.get("https://www.quizizz.com/login")

    # Login Screen -> Choose Email Option -> Create Quiz Screen
    driver.find_element(By.CLASS_NAME, 'email').click()
    emailTxt = driver.find_element(By.NAME, "Enter email address or username")
    passdTxt = driver.find_element(By.NAME, "Password")
    emailTxt.clear()
    passdTxt.clear()
    emailTxt.send_keys("minh0608@outlook.com")
    passdTxt.send_keys("minh0608")
    try:
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

        # ================= LOOP FOR EACH QUESTION ================
        creatingScreen = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="__layout"]/div/div[3]/main/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/button'))
        )
        driver.find_element(By.XPATH,
                            '//*[@id="__layout"]/div/div[3]/main/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/button').click()
        breakpoint()
    except exc.TimeoutException:
        print("Connection got time out ;-;")


if __name__ == '__main__':
    main(LINE_TEST)

"""
TODO MAIN LIST:
- Add module for each scan tests in content folder
- Add expected output in src folder
- Add some kind of hook so it can access the internet and automatically generate the quiz
"""
