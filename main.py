from datetime import datetime
from PyPDF2 import PdfReader
import subprocess
import os
from datetime import datetime
import os
import pyttsx3
#from TTS.api import TTS
from datetime import datetime
import os
def tts_mp3(text, folder_path):
    os.makedirs(folder_path, exist_ok=True)

    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.mp3")
    file_path = os.path.join(folder_path, filename)

    engine = pyttsx3.init()

    # Female voice select
    voices = engine.getProperty("voices")
    for voice in voices:
        if "female" in voice.name.lower() or "zira" in voice.name.lower():
            engine.setProperty("voice", voice.id)
            break

    engine.save_to_file(text, file_path)
    engine.runAndWait()

    return file_path
'''
def coqui_tts(text, folder_path):
    os.makedirs(folder_path, exist_ok=True)

    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.wav")
    file_path = os.path.join(folder_path, filename)

    tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")
    tts.tts_to_file(text=text, file_path=file_path)

    return file_path
'''
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def remove_pdf(filename):
    if filename.lower().endswith(".pdf"):
        return filename[:-4]
    return filename

def save_text(text, folder_path):
    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.txt")
    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(folder_path, filename)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)

    return file_path

def pdf_extract(folder_path, pdfname, initial_page, final_page):
    pdf_path = os.path.join(folder_path, pdfname)

    reader = PdfReader(pdf_path)
    text = ""

    for i in range(initial_page - 1, final_page):
        text += reader.pages[i].extract_text()

    return text

def select_file(folder_path):
    files = [f for f in os.listdir(folder_path)
             if os.path.isfile(os.path.join(folder_path, f))]

    if not files:
        raise FileNotFoundError("No files found in the folder")

    for index, file in enumerate(files, start=1):
        print(f"{index}. {file}")

    while True:
        try:
            choice = int(input("Select file number: "))
            if 1 <= choice <= len(files):
                return files[choice - 1]
            print("Invalid selection")
        except ValueError:
            print("Enter a valid number")

def llama3(prompt):
    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt.encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return result.stdout.decode("utf-8", errors="ignore").strip()
