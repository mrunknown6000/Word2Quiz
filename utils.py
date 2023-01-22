# This code was made by MrUnknown6000

import docx2txt
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as exc
from selenium.webdriver.common.action_chains import ActionChains
import json
import os


# Section For Configuration Options
# * Load Configuration File Attempt
def loadConfig() -> dict or None:
    CONF_DIR = os.getenv('APPDATA') + '\\word2quiz-conf.json'
    loadedConfig = {}
    try:
        with open(CONF_DIR, 'r', encoding='UTF-8') as f:
            loadedConfig = json.load(f)
            return loadedConfig
    except FileNotFoundError:
        with open(CONF_DIR, 'x') as f:
            pass


def writeConfig() -> None:
    pass


# Section For The Algorithms
def convertDoc2Txt(doc_direct: str) -> str:
    try:
        text = docx2txt.process(doc_direct)
        return text
    except PermissionError:
        print("ERROR: Permission Denied")
        exit(1)
    except FileNotFoundError:
        print("ERROR: File Not Found")
        exit(1)


def filterer(raw_string_inp: str) -> str:
    finalized = raw_string_inp
    while finalized.find("\n\n") != -1:
        finalized = finalized.replace("\n\n", "\n")
    return finalized


def questionIdentification(formatted_string: str, config: dict) -> dict:
    finalized = {}
    formatted_string += f" {config['keys']['headmark']} !@#$%^&*"
    wordsByWord = formatted_string.split()
    HEADER_CHAR = config['keys']['headmark']
    SPECIAL_CHAR = config['keys']['ansmark']
    OPTION_KEYS = config['keys']['options']

    titleCounter = 0
    titleList = []
    temporaryStringIdentifier = ""
    optionList = []
    answerList = []
    temporaryList = []
    # Filtered Everything
    for word in wordsByWord:
        if (OPTION_KEYS[0] in word) or (OPTION_KEYS[1] in word) or (OPTION_KEYS[2] in word) or (OPTION_KEYS[3] in word):
            # Check if the ID is title:
            if titleCounter == 0 or ((titleCounter % 4) == 0):
                titleList.append(temporaryStringIdentifier)
            else:  # Check if it not title
                if SPECIAL_CHAR in temporaryStringIdentifier:
                    answerList.append(temporaryStringIdentifier.replace(SPECIAL_CHAR, ""))
                    temporaryList.append(temporaryStringIdentifier.replace(SPECIAL_CHAR, ""))
                else:
                    temporaryList.append(temporaryStringIdentifier)

            temporaryStringIdentifier = ""
            titleCounter += 1
        elif word == HEADER_CHAR:
            if titleCounter != 0:
                if SPECIAL_CHAR in temporaryStringIdentifier:
                    answerList.append(temporaryStringIdentifier.replace(SPECIAL_CHAR, ""))
                    temporaryList.append(temporaryStringIdentifier.replace(SPECIAL_CHAR, ""))
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
        print("ERROR: Filter Indexer failed")
    return finalized


# Networking Algorithms
def connectionApplier(driver, questions_dictionary, email, password):
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
    emailTxt.send_keys(email)
    passdTxt.send_keys(password)
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

        for questionStack in questions_dictionary.values():
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
            if questionStack['title'] == questions_dictionary[len(questions_dictionary) - 1]['title']:
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
        quitConfirmation = input("Please complete the procedure of saving the quiz then press enter to quit... ")
        if quitConfirmation == '':
            print('Thank for using the programing | Credit: MrUnknown6000')
            driver.close()
    #     USER INPUT
    except exc.TimeoutException:
        print("ERROR: Timeout")
