from utils import *


def main(doc_dir):
    print(convertDoc2Txt(doc_dir))


if __name__ == '__main__':

    # ? Current Available Configuration: Table Variations and Line By Line
    inputDoc = r"C:\Users\admin\.src-code\python\Word2Quiz\content\test.docx"
    main(inputDoc)

"""
TODO MAIN LIST:
- Add module for each scan tests in content folder
- Add expected output in src folder
- Add some kind of hook so it can access the internet and automatically generate the quiz
"""