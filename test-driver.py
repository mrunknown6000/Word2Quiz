from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as exc
from selenium.webdriver.common.action_chains import ActionChains

case1 = {
    0: {'title': 'Câu 1: Châu Á tiếp giáp với những châu lục nào dưới đây ?', 'answer': ' Châu Âu, Châu Phi.',
        'options': [' Châu Phi, Châu Đại Dương.', ' Châu Mĩ, Châu Âu.', ' Châu Âu, Châu Phi.',
                    ' Châu Mĩ, Châu Phi.']},
    1: {'title': 'Câu 2: Châu Á không tiếp giáp với đại dương nào sau đây', 'answer': ' Đại Tây Dương.',
        'options': [' Thái Bình Dương.', ' Ấn Độ Dương.', ' Bắc Băng Dương.', ' Đại Tây Dương.']},
    2: {'title': 'Câu 3: Các núi và sơn nguyên cao của châu Á tập trung chủ yếu ở', 'answer': ' vùng trung tâm.',
        'options': [' vùng trung tâm.', ' vùng phía đông.', ' vùng phía tây.', ' phía bắc.']}}

# LOGIN INFO: minh0608@outlook.com | minh0608
driver = webdriver.Chrome()
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

    for questionStack in case1.values():
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
        if questionStack['title'] == case1[len(case1)-1]['title']:
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

