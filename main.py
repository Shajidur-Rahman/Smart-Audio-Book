# first install the python pakegs:1. pip install pyttsx3
#                                 2. pip install PyPDF2
import pyttsx3
import PyPDF2

book = open('eng.pdf', 'rb') # if you want to add your pdf than change the name {book = open('your_book_name.pdf', 'rb')}
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
speaker = pyttsx3.init()
voices = speaker.getProperty('voices') #if you want to change the voice than remove this line and under this line
speaker.setProperty('voice', voices[1].id)# if you remove this {voices = speaker.getProperty('voices')} then also remove this
for num in range(6, pages): #chose your favorite page number {for num in range(your_page_number, pages):}
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()