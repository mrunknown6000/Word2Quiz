from utils import *

# FORMAT_TEST = r'C:\Users\admin\.src-code\python\Word2Quiz\content\scan-formatstyle.docx'
LINE_TEST = r'C:\Users\admin\.src-code\python\Word2Quiz\content\scan-linebyline.docx'
TABLE_TEST = r'C:\Users\admin\.src-code\python\Word2Quiz\content\scan-table.docx'

GEO_CASE = r'C:\Users\admin\.src-code\python\Word2Quiz\content\testcasegeo.docx'
BIO_CASE = r'C:\Users\admin\.src-code\python\Word2Quiz\content\testcasebio.docx'


def main(doc_dir):
    print(convertDoc2Txt(doc_dir))


if __name__ == '__main__':
    print(f"Line Test==========: \n {convertDoc2Txt(GEO_CASE)}")

    # main(inputDoc)

"""
TODO MAIN LIST:
- Add module for each scan tests in content folder
- Add expected output in src folder
- Add some kind of hook so it can access the internet and automatically generate the quiz
"""
