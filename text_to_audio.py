import pyttsx3
import PyPDF2

book=open('soceer_ml.pdf','rb')
pdfreader=PyPDF2.PdfFileReader(book)
pages=pdfreader.numPages
#print("Total no. of pages in the pdf:",pages)
page=pdfreader.getPage(3)
text=page.extractText()
speaker=pyttsx3.init()
speaker.say(text)
speaker.runAndWait()