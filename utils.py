import docx2txt
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as exc
from selenium.webdriver.common.action_chains import ActionChains


def convertDoc2Txt(doc_direct: str) -> str:
    try:
        text = docx2txt.process(doc_direct)
        return text
    except PermissionError:
        print("Lỗi | Truy cập bị từ chối")
        exit(1)
    except FileNotFoundError:
        print("Lỗi | File không tồn tại")
        exit(1)


def filterer(raw_string_inp: str) -> str:
    finalized = raw_string_inp
    while finalized.find("\n\n") != -1:
        finalized = finalized.replace("\n\n", "\n")
    return finalized


def questionIdentification(formatted_string: str) -> dict:
    finalized = {}
    formatted_string += " Câu 69420"
    wordsByWord = formatted_string.split()
    SPECIAL_CHAR = "<-"

    titleCounter = 0
    titleList = []
    temporaryStringIdentifier = ""
    optionList = []
    answerList = []
    temporaryList = []
    # Filtered Everything
    for word in wordsByWord:
        if ("A." in word) or ("B." in word) or ("C." in word) or ("D." in word):
            # Check if the ID is title:
            if titleCounter == 0 or ((titleCounter % 4) == 0):
                titleList.append(temporaryStringIdentifier)
            else:  # Check if it not title
                if SPECIAL_CHAR in temporaryStringIdentifier:
                    answerList.append(temporaryStringIdentifier.replace("<-", ""))
                    temporaryList.append(temporaryStringIdentifier.replace("<-", ""))
                else:
                    temporaryList.append(temporaryStringIdentifier)

            temporaryStringIdentifier = ""
            titleCounter += 1
        elif word == "Câu":
            if titleCounter != 0:
                if SPECIAL_CHAR in temporaryStringIdentifier:
                    answerList.append(temporaryStringIdentifier.replace("<-", ""))
                    temporaryList.append(temporaryStringIdentifier.replace("<-", ""))
                else:
                    temporaryList.append(temporaryStringIdentifier)
                optionList.append(temporaryList)
                temporaryList = []
            temporaryStringIdentifier = ""
            temporaryStringIdentifier += word
        else:
            temporaryStringIdentifier += " " + word
    del temporaryList, temporaryStringIdentifier, titleCounter
    titleList = tuple(titleList)
    optionList = tuple(optionList)
    answerList = tuple(answerList)
    try:
        for questionId in range(len(titleList)):
            finalized[questionId] = {}
            finalized[questionId]["title"] = titleList[questionId]
            finalized[questionId]["answer"] = answerList[questionId]
            finalized[questionId]["options"] = optionList[questionId]
    except IndexError:
        print("Lỗi | Lỗi ký hiệu, kiểm tra lại file")

        # print(titleList)
        # print(optionList)
    return finalized


def connectionApplier(driver, questions_dictionary, email, password):
    driver.get("https://www.quizizz.com/login")
    actions = ActionChains(driver)
    print('Đang kết nối vào quizizz.com...')
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
    emailTxt.send_keys(email)
    passdTxt.send_keys(password)
    try:
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'continue-button'))
        )
        driver.find_element(By.CLASS_NAME, 'continue-button').click()
        print('Đang đăng nhập vào tài khoản Quizzi...')
        # Keyboard Navigate to Quiz Generate Area
        # driver.implicitly_wait(4)
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'admin-external-link'))
        )
        driver.find_element(By.CLASS_NAME, 'admin-external-link').click()
        print('Đang vào menu tạo Quiz...')
        # ? ================= LOOP FOR EACH QUESTION ================
        # Initial Loop hole
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="__layout"]/div/div[3]/main/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/button'))
        )
        driver.find_element(By.XPATH,
                            '//*[@id="__layout"]/div/div[3]/main/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/button').click()

        for questionStack in questions_dictionary.values():

            # ? ================================= WRITE THE QUESTION AND THE ANSWER =================================
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="questionQuery"]'))
            )

            # Interact
            driver.find_element(By.XPATH, '//*[@id="questionQuery"]').click()
            actions.send_keys(questionStack['title'])
            actions.perform()
            for i in range(len(questionStack['options'])):
                driver.find_element(By.ID, f"option-{i}").click()
                actions.send_keys(questionStack['options'][i])
                actions.perform()
                if questionStack['options'][i] == questionStack['answer']:
                    driver.find_element(By.XPATH,
                                        f"//*[@id=\"__layout\"]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div/div[3]/div/ul/li[{i + 1}]/div/div[1]/div[3]/button").click()
            driver.find_element(By.XPATH,
                                '//*[@id="__layout"]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/button').click()
            # ? ================================= ONE QUESTION LOOP DONE =================================

            # ? ================================= GENERATING A NEW CYCLE =================================
            if questionStack['title'] == questions_dictionary[len(questions_dictionary) - 1]['title']:
                break
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located(
                    (By.XPATH,
                     '//*[@id="__layout"]/div/div[3]/main/div[1]/div[1]/div[2]/div[3]/div/div/div[2]/div[3]/div/button'))
            )
            driver.execute_script('arguments[0].click();', driver.find_element(By.XPATH,
                                                                               '//*[@id="__layout"]/div/div[3]/main/div[1]/div[1]/div[2]/div[3]/div/div/div[2]/div[3]/div/button'))
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((
                    By.XPATH, '//*[@id="__layout"]/div/div[3]/div/div/div/div/div[2]/div[1]/button'
                ))
            )
            driver.execute_script('arguments[0].click();', driver.find_element(By.XPATH,
                                                                               '//*[@id="__layout"]/div/div[3]/div/div/div/div/div[2]/div[1]/button'))
        #     ? ===================================== COMPLETED ALL QUESTION ==============================================================
        print('================================= Đã Làm Quiz xong! =================================')
        print('Hãy lưu lại Quiz và tắt cửa số trình duyệt')
        input('Ấn Enter để thoát...')
        driver.quit()
        print('Cảm ơn đã sử dụng - Credit: MrUnknown850')

    except exc.TimeoutException:
        print("Lỗi | Mạng chậm quá .-.")
