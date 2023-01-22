# This code was made by MrUnknown6000

from utils import *
from selenium import webdriver


def main(doc_dir, password, email, config):
    currentDocxString = convertDoc2Txt(doc_dir)
    currentDocxString = filterer(currentDocxString)
    finalizedDictionary = questionIdentification(currentDocxString, config)
    print('Document Type-safe check verified...')
    print("Processing...")
    driver = webdriver.Chrome()
    connectionApplier(driver, finalizedDictionary, email, password)


if __name__ == '__main__':
    # * Pre-load Data Section | Configurations and GUI
    # User Interface Loaded
    print("==== WORD TO QUIZ GENERATOR | Credit To MrUnknown6000 ====")
    wordInput = input("Type the Directory to your Word Document: ")

    temporal = loadConfig()
    # * Query for default configuration
    print('Saved Email:', temporal['email'])
    print('Password:', temporal['pass'])
    if input('Do you want to use default configuration? [y/n]: ') in ['n', 'N']:
        emailInp = input("Type your Quizzi account's email: ")
        passdInp = input("Type your Quizzi account's password: ")
    else:
        emailInp = temporal['email']
        passdInp = temporal['pass']

    main(wordInput, passdInp, emailInp, temporal)
