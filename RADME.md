**AI Summarizer and Keywordizer**

What is this?
This project summarizes your text files and generates a response file named Response.txt with Keywords and Summary of size that you choose.

Why ?
The most important thing is time and it is common being busy and also many people dont go through documents since they are lengthy and reading them for long may endup losing flow and interest.So, instead of we manually going through those lengthy documents how would it be if someone does it and gives us insights in the form of summary and keywords. Thats how we came up with this **AI Summarizer and Keywordizer**.

Techstacks:
python

Prerequisites:
Python 3.9 or higher is required.
An internet connection is needed.

Setup gemini api:
Get a free API key from Google AI Studio.
Set the environment variable in your terminal:
        export GEMINI_API_KEY='your_api_key_here'


Installation:
run pip install -r requirements.txt in terminal.

Api used: gemini-3-flash-preview

Project Flow:
1.Place your text that needs to be worked on in a text file
2.Validation of file with exception raised if something goes wrong like unable to find file.
3.Text extraction from the input file.
4.Choosing the desired choice for size of result.
4.Validation of non empty text.
5.Summarising text.
6.Extracting keywords.
7.Writing into new file. 

Command to run in terminal to intiate program: python project.py
Example input format:  input.txt

Functions?                             
In the *main* function it validates if the file path is accessible or not. After validating it extract the text it asks the user to choose the size of the summary by providing options small,medium and long.After validating if the user entered the valid size the text is then passe to *summarize* function which after validating if the text is there or not and returns the summary back. Then the same original text is passed to *Keywordize* function which also validates the text and returns back keywords in the format one keyword per line.These summary and keywords are then entered into a new file named *Response.txt* so that user can go through it whenever he wants to.

When does the project raises error?
Invalid input file path   => *FileNotFoundError* with message: Error : Failed to find file
Invalid choice of size   => *ValueError* with message: Enter 1 or 2 or 3 only
Empty text in the input file   => *ValueError* with message: Empty text
Any other error is also handled and printed usind try and except.

Design choice:
Feature of choosing size to facilitate the proper direction through prompting the user and to make the output flexible.
Not allowing Empty text to pass into ai conversation in summarize and keywordize function because the api credits waste unnecessarily.
Navigation to size, summarize and keywordize functions directly from main in order to give professional structure to the project in this way the code can be navigated and exceptions can be handled efficiently.

Why the output isnt just printed instead wrote in a new Response.txt file?
The printed output is accessible only till stay on that terminal,but the file stays even after closing the whole terminals and project. it is stoded in Secondary storage and we can access whenever we wish to and it can also be shared to others easily.


Drawbacks:
There can be error if the api calling takes time more than expected.
There can be exception if the api credits reach limit for that specific 24 hrs of period.

Verification from developer end: 
A pytest file is also programmed that can be checked for functionalities of functions in main file.

I learned about api integration and the role of prompt aligned to the project. it taught me to document as documenting this file is the first ever for me. It taught me very important that a meaningful function is built if the heirarchy of functions , the clear input and output that should be returned comes from "Purpose" and it can be clearly understood if the heirarchy or structure is solid.
The things that broke were the clarity in designing the size function but with the clarity in its purpose and structure it was done properly later.
Add more features like ability to choose whether the output is required for long term use i.e. text file or temporary i.e. in the terminal.

Conclusion:
With the help of artificial intelligence aided by efffective prompting and the proper data handling using python an AI summarizer and Keywordizer is built.