from utils import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as exc
from selenium.webdriver.common.action_chains import ActionChains

# FORMAT_TEST = r'C:\Users\admin\.src-code\python\Word2Quiz\content\scan-formatstyle.docx'
LINE_TEST = r'C:\Users\admin\.src-code\python\Word2Quiz\content\scan-linebyline.docx'
TABLE_TEST = r'C:\Users\admin\.src-code\python\Word2Quiz\content\scan-table.docx'
GEO_CASE = r'C:\Users\admin\.src-code\python\Word2Quiz\content\testcasegeo.docx'

# Networking Configuration
driver = webdriver.Chrome()


def main(doc_dir):
    currentDocxString = convertDoc2Txt(doc_dir)
    currentDocxString = filterer(currentDocxString)
    finalizedDictionary = questionIdentification(currentDocxString)


    global driver
    driver.get("https://www.quizizz.com/login")
    actions = ActionChains(driver)

    # Login Screen -> Choose Email Option -> Create Quiz Screen
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((
            By.CLASS_NAME, 'email'
        ))
    )
    driver.find_element(By.CLASS_NAME, 'email').click()
    emailTxt = driver.find_element(By.NAME, "Enter email address or username")
    passdTxt = driver.find_element(By.NAME, "Password")
    emailTxt.clear()
    passdTxt.clear()
    emailTxt.send_keys("minh0608@outlook.com")
    passdTxt.send_keys("minh0608")
    try:
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'continue-button'))
        )
        driver.find_element(By.CLASS_NAME, 'continue-button').click()

        # Keyboard Navigate to Quiz Generate Area
        # driver.implicitly_wait(4)
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'admin-external-link'))
        )
        driver.find_element(By.CLASS_NAME, 'admin-external-link').click()

        # ================= LOOP FOR EACH QUESTION ================
        # Initial Loop hole
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="__layout"]/div/div[3]/main/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/button'))
        )
        driver.find_element(By.XPATH,
                            '//*[@id="__layout"]/div/div[3]/main/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/button').click()

        for questionStack in finalizedDictionary.values():
            # Actually Process all the question
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="questionQuery"]'))
            )

            # Interact
            driver.find_element(By.XPATH, '//*[@id="questionQuery"]').click()
            actions.send_keys(questionStack['title'])
            actions.perform()
            for i in range(len(questionStack['options'])):
                driver.find_element(By.XPATH, f'//*[@id="option-{i}"]').click()
                actions.send_keys(questionStack['options'][i])
                actions.perform()
                if questionStack['options'][i] == questionStack['answer']:
                    driver.find_element(By.XPATH,
                                        f'//*[@id="__layout"]/div/div[3]/div/div/div/div/div/div/div[2]/div[1]/div/div[3]/div/ul/li[{i + 1}]/div/div[1]/div[3]/button').click()
            # Save Button
            driver.find_element(By.XPATH,
                                '//*[@id="__layout"]/div/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/button').click()
            # New Question Wizard
            if questionStack['title'] == finalizedDictionary[len(finalizedDictionary) - 1]['title']:
                break
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, 'quick-add-action'))
            )
            driver.execute_script('arguments[0].click();', driver.find_element(By.CLASS_NAME, 'quick-add-action'))
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((
                    By.XPATH, '//*[@id="__layout"]/div/div[3]/div/div/div/div/div[2]/div[1]/button'
                ))
            )
            driver.execute_script('arguments[0].click();', driver.find_element(By.XPATH,
                                                                               '//*[@id="__layout"]/div/div[3]/div/div/div/div/div[2]/div[1]/button'))

        breakpoint()
    #     USER INPUT
    except exc.TimeoutException:
        print("Connection got time out ;-;")


if __name__ == '__main__':
    wordInput = r'C:\Users\admin\.src-code\python\Word2Quiz\geo.docx'
    main(wordInput)

"""
TODO MAIN LIST:
- Add module for each scan tests in content folder
- Add expected output in src folder
- Add some kind of hook so it can access the internet and automatically generate the quiz
"""
