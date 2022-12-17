import docx2txt

""" TEXT CONVERSION INFRASTRUCTURE
- Convert .docx file into raw string text                   CHECKED
- Removing all whitespace                                   CHECKED 
- Question Identification Filterer:                         PENDING
  + Trigger Word: "Câu", "A.", "B.", "C.", "D."
  + Answer Identification: Manual Notation ;-;
- Dictionary Filtering:
  + Key <Question No.> -> Deeper Level Dictionary
    * Title: "String"
    * CorrectAns: 0->3 (ABCD)
    * List all answer
Eg: 
1: {
  title: "This is a title",
  correctAns: "A",
  options: ["Answer1", "Answer2", "Answer3", "Answer4"]
}
"""


def convertDoc2Txt(doc_direct: str) -> str:
    try:
        text = docx2txt.process(doc_direct)
        text = filterer(text)
        return text
    except Exception:
        print("Error Occurred While Converting!")
        exit(1)


def filterer(raw_string_inp: str) -> str:
    finalized = raw_string_inp
    while finalized.find("\n\n") != -1:
        finalized = finalized.replace("\n\n", "\n")
    return finalized


def questionIdentification(formated_string: str) -> dict:
    finalized = {}
    return finalized
