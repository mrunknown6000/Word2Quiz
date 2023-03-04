from utils import *
from selenium import webdriver


def main(doc_dir, password, email, driver):
    currentDocxString = convertDoc2Txt(doc_dir)
    currentDocxString = filterer(currentDocxString)
    finalizedDictionary = questionIdentification(currentDocxString)
    if opt == '1':
        driver = webdriver.Chrome()
    elif opt == '2':
        driver = webdriver.ChromiumEdge()
    elif opt == '3':
        driver = webdriver.Firefox()

    connectionApplier(driver, finalizedDictionary, email, password)


if __name__ == '__main__':
    print('========== Word2Quiz - Credit: MrUnknown6000 ==========')
    opt = browser = None
    while opt not in ['1', '2', '3']:
        print('=== Chọn trình duyệt: === \n 1. Chrome \t 2. Edge \t 3. Firefox')
        opt = input('Chọn số: ')

    wordInput = input("Gõ đường dẫn file Word: ")
    emailInp = input("Gõ email tài khoản Quizzi của bạn: ")
    passdInp = input("Gõ mật khẩu tài khoảng Quizzi của bạn: ")

    main(wordInput, passdInp, emailInp, opt)

"""
TODO MAIN LIST:
- Add module for each scan tests in content folder
- Add expected output in src folder
- Add some kind of hook so it can access the internet and automatically generate the quiz
"""
