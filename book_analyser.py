from main import save_text
from main import select_file
from main import pdf_extract
from main import llama3
from main import speak
from main import tts_mp3
from datetime import time
from main import remove_pdf
#from main import coqui_tts
book_name = select_file("Books")
ip = int(input("Initial Pg:    "))
fp = int(input("Final Pg:    "))
'''print(book_name)
print(type(ip))'''
#fdd = f"Books\{book_name}"
pdf_text = pdf_extract("Books", book_name,  ip, fp)

opt = input("1. Test\n2. Summarise and easy Explanation\n3. Speak Summarisation\n4. Simple TTS\n")
if opt=="1":
    qsn = input(" Number of questions : ")
    ins1 = f"I have read the paragraph given below and I want you to take the test. just print questions that helps me revise the concept.. nothing else. Keep the number of questions as {qsn} \n"
    out = llama3(ins1 + pdf_text)
    path = f'Books/{remove_pdf(book_name)}/Tests'
    save_text(out, path)
    print("File is Saved")
elif opt=="2":
    qsn = input("Word Limit : ")
    ins1 = f" Summarize the following paragraph in easy words so that I can understand in {qsn} words."
    out = llama3(ins1 + pdf_text)
    path = f'Books/{remove_pdf(book_name)}/Summary'
    save_text(out, path)
    print("File is Saved")
elif opt=="3":
    qsn = input("Word Limit : ")
    ins1 = f" Summarize the following paragraph in easy words so that I can understand in {qsn} words. dont make points. give it in continuos paragraph format."
    out = llama3(ins1 + pdf_text)
    path = f'Books/{remove_pdf(book_name)}/AI TTS/'
    tts_mp3(out, path)
    save_text(out, path)
    print("File is Saved")
    speak("file is saved")
elif opt=="4":
    path = f'Books/{remove_pdf(book_name)}/TTS/'
    tts_mp3(pdf_text, path)
    speak("File is saved.")
else:

    print("Please try again...")
