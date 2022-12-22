from utils import *
from selenium import webdriver

def main(doc_dir, password, email):
    currentDocxString = convertDoc2Txt(doc_dir)
    currentDocxString = filterer(currentDocxString)
    finalizedDictionary = questionIdentification(currentDocxString)
    driver = webdriver.Chrome()
    connectionApplier(driver, finalizedDictionary, email, password)


if __name__ == '__main__':
    wordInput = input("Gõ đường dẫn file Word: ")
    emailInp = input("Gõ email tài khoản Quizzi của bạn: ")
    passdInp = input("Gõ mật khẩu tài khoảng Quizzi của bạn: ")

    # main(wordInput, passdInp, emailInp)

"""
TODO MAIN LIST:
- Add module for each scan tests in content folder
- Add expected output in src folder
- Add some kind of hook so it can access the internet and automatically generate the quiz
"""
