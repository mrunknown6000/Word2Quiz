import docx2txt


def convertDoc2Txt(doc_direct: str) -> str:
    try:
        text = docx2txt.process(doc_direct)
        return text
    except PermissionError:
        print("Error: File Access Denial!")
        exit(1)
    except FileNotFoundError:
        print("Error: File Not Found")
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
        print("Error: Failed to filtering the file")

        # print(titleList)
        # print(optionList)
    return finalized

