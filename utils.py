import docx2txt


# TODO: Add Exception + Write Test Unit
def convertDoc2Txt(doc_direct: str) -> str:
    text = docx2txt.process(doc_direct)
    return text


def textAnalyzer(string_inp: str) -> dict:
    analyzedStr = {}

    """
    3 Stage of Analysis:
    - Removing Duplicate "\n"
    - Line -> Question Identification
    - Sort into a dictionary
    """

    return analyzedStr
