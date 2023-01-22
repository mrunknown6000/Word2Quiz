from turtle import color

from utils import *
from selenium import webdriver
import tkinter as tk


def main(doc_dir, password, email):
    currentDocxString = convertDoc2Txt(doc_dir)
    currentDocxString = filterer(currentDocxString)
    finalizedDictionary = questionIdentification(currentDocxString)
    driver = webdriver.Chrome()
    connectionApplier(driver, finalizedDictionary, email, password)


if __name__ == '__main__':
    guiWindow = tk.Tk()
    guiWindow.title('Word2Quiz | By MrUnknown850')
    guiWindow.geometry("300x175")
    guiWindow.minsize(300, 175)
    guiWindow.maxsize(300, 175)

    fileText = tk.Label(guiWindow, text="Directory: ", font=24)
    fileEntry = tk.Entry(guiWindow, font=24)
    emailText = tk.Label(guiWindow, text="Email: ", font=24)
    emailEntry = tk.Entry(guiWindow, font=24)
    passText = tk.Label(guiWindow, text="Password: ", font=24)
    passEntry = tk.Entry(guiWindow, font=24, show="*")
    executeBtn = tk.Button(guiWindow, text="Start :)", width=15, height=3, font=30)
    otherBtn = tk.Button(guiWindow, text="Other...", width=15, height=3, font=30)

    emailText.grid(row=0, column=0, pady=2, sticky="W")
    passText.grid(row=1, column=0, pady=2, sticky="W")
    fileText.grid(row=2, column=0, pady=2, sticky="W")
    emailEntry.grid(row=0, column=1, sticky="W", pady=4)
    passEntry.grid(row=1, column=1, sticky="W", pady=4)
    fileEntry.grid(row=2, column=1, sticky="")
    executeBtn.grid(row=3, column=0, sticky="W", pady=10)
    otherBtn.grid(row=3, column=1, sticky="W", pady=10)

    guiWindow.mainloop()

    # wordInput = input("Gõ đường dẫn file Word: ")
    # emailInp = input("Gõ email tài khoản Quizzi của bạn: ")
    # passdInp = input("Gõ mật khẩu tài khoảng Quizzi của bạn: ")

    # main(wordInput, passdInp, emailInp)

"""
TODO MAIN LIST:
- Add module for each scan tests in content folder
- Add expected output in src folder
- Add some kind of hook so it can access the internet and automatically generate the quiz
"""
