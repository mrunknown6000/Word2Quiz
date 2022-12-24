# Word2Quiz - A Solution for long boring repetitive task of making Quiz from a Word file
For all the one who have tirely copying questions by questions for 4-6 hours straight doing nothing just copying which can be both ineffective and inefficient. So this program gonna help yall so no more boring copying lol.

## Installation
You can download this at [the release]{https://github.com/mrunknown6000/Word2Quiz/releases/tag/stable} and yes, no installation. This is a standalone program so you only need to execute this from your command line.

## How To Use
1. Download the executable from [the release page]{https://github.com/mrunknown6000/Word2Quiz/releases/tag/stable}.
2. Preparing the word file according to the file format below.
3. Type in the directory, email and password for your quizzi account.
4. After the automation process done, do manual saving then press Enter to quit out of the program.

## Word File Format (Only Vietnamese supported)
| **Trigger Word** | **Purpose**|
|------------------|------------|
| Câu              | Indicate the begining of a question|
| A. B. C. D.      | Saving as option for your question. Warning, **D.** is the trigger for the end of a question|
| <- | This mark the answer for each question|
##### **Warning**: The program have a type safe check to make sure that every question have each of these Trigger before proceed to the execution part. Please make sure that you have all of these word available right in your document
##### **Warning 2**: Microsoft Office Word in any version have a feature call Automatic Numbering. To make sure this doesn't occur. Please paste your entire Word file into a notepad to get rid of all Automatic Numbering then paste it back into the word file to proceed.

## Error Codes
| **Error Codes** | **Meaning and Fixes** |
| ----------------|-----------------------|
| Permission Denied| A different program is using the file. Please check if any program is using it and close it before proceed.|
| File Not Found | The file you put in the directory when the program ask you to is no where to be found using the given directory. Check the Word file directory then run the program again|
| Filter Indexer failed| There is an error found using the built-in type safe check. Check your Word document and follow the Word File Format above|
| Timeout | This error occur when a website take too long to load a needed element for Selenium to send action to. You might need to switch your network or close program that taking alot of bandwidth. (Timeout durration is 30 seconds per pages)
